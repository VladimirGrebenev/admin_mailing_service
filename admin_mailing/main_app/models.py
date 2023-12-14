from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import process_dispatches

phone_number_validator = RegexValidator(
    regex=r'^7\d{10}$',
    message='Номер телефона должен быть в формате 7XXXXXXXXXX'
)

time_zone_validator = RegexValidator(
    regex=r'^GMT\+\d{2}$',
    message='time_zone должен быть в формате GMT+XX'
)

operator_code_validator = RegexValidator(
    regex=r'^\d{3}$',
    message='Код мобильного оператора должен состоять из трех цифр'
)


class Client(models.Model):
    uu_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                             editable=False)
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[phone_number_validator]
    )
    operator_code = models.CharField(
        max_length=3,
        validators=[operator_code_validator]
    )
    tag = models.CharField(max_length=50)
    timezone = models.CharField(
        max_length=10,
        validators=[time_zone_validator]
    )


# def validate_client_filter(value):
#     # Проверка условий валидации
#     if not value.startswith('operator_code:') and not value.startswith('tag:'):
#         raise ValidationError(
#             'Фильтр клиентов должен начинаться с "operator_code:" или "tag:"')


class Dispatch(models.Model):
    '''
    Класс Рассылки(Dispatch), при его создании автоматически создаются объекты
    класса Сообщения(Message).
    ...
    Атрибуты
    --------
    uu_id : uuid4
        уникальный pk
    start_datetime : DateTimeField 'YYYY-MM-DD HH:MM'
        начало рассылки
    end_datetime : DateTimeField 'YYYY-MM-DD HH:MM'
        конец рассылки
    message_text : TextField
        текст сообщения рассылки
    tag_filter : str
        произвольный тег для фильтрации клиентов
    operator_code_filter: str
        код оператора для фильтрации клиентов
    '''
    uu_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                             editable=False)
    start_datetime = models.DateTimeField(
        help_text=("Введите дату и время старта в формате 'YYYY-MM-DD HH:MM'")
    )
    message_text = models.TextField()
    tag_filter = models.CharField(max_length=50, blank=True)
    operator_code_filter = models.CharField(max_length=3, blank=True)
    end_datetime = models.DateTimeField(
        help_text=("Введите дату и время финиша в формате 'YYYY-MM-DD HH:MM'")
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создание сообщений при сохранении рассылки
        clients = Client.objects.all()

        if self.tag_filter:
            clients = clients.filter(tag=self.tag_filter)

        if self.operator_code_filter:
            clients = clients.filter(operator_code=self.operator_code_filter)

        for client in clients:
            dispatch = Dispatch.objects.get(uu_id=self.uu_id)
            message = Message.objects.create(dispatch=dispatch,
                                             client=client)

    # валидация времени окончания рассылки (must be time.now() + 5 минут)
    def clean(self):
        start_datetime = datetime.strptime(self.start_datetime, "%Y-%m-%dT%H:%M")
        end_datetime = datetime.strptime(self.end_datetime, "%Y-%m-%dT%H:%M")
        if end_datetime <= datetime.now(timezone.utc) + timedelta(minutes=5):
            raise ValidationError(
                "Минимальное время окончания должно быть больше текущего времени плюс 5 минут.")
        if start_datetime >= end_datetime:
            raise ValidationError(
                "Время окончания должно быть больше времени начала.")
        if end_datetime <= start_datetime + timedelta(minutes=5):
            raise ValidationError(
                "Интервал между временем начала и окончания должен быть не меньше 5 минут.")


@receiver(post_save, sender=Dispatch)
def process_dispatches_on_create(sender, instance, created, **kwargs):
    if created:
        process_dispatches.delay()


class Message(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    send_status = models.BooleanField(default=False)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
