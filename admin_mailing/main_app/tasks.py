import requests
from celery import shared_task
from datetime import datetime
from django.utils import timezone
from admin_mailing.settings import TOKEN_BEARER, URL_SENDING_API_SERVICE


@shared_task
def process_dispatches():
    """Функция инициализации рассылок"""
    from .models import Dispatch, Message, Client
    print(f'стартовал process_dispatches: {datetime.now(timezone.utc)}')
    current_time = timezone.now()
    # фильтруем рассылки которые должны быть активированы
    active_dispatches = Dispatch.objects.filter(
        start_datetime__lte=current_time,
        end_datetime__gte=current_time
    )

    for dispatch in active_dispatches:
        # собираем в рассылке сообщения которые ещё не были отправлены
        messages = Message.objects.filter(dispatch=dispatch.uu_id,
                                          send_status=False)

        for message in messages:
            try:
                # Отправка сообщения на сторонний сервис
                send_message_to_client(message)
                message.send_status = True
            except Exception as e:
                handle_message_error(message, e)
                # Обработка ошибок при отправке сообщений
                # Логирование ошибок


@shared_task
def send_message_to_client(message):
    """Функция отправки сообщения через сторонний API сервис"""
    # Логика отправки сообщения клиенту
    # внешний сервис и передаём необходимые данные:
    url = f"{URL_SENDING_API_SERVICE}{message.id}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_BEARER}"
    }
    data = {
        "id": message.id,
        "phone": message.client.phone_number,
        "text": message.dispatch.message_text
    }
    response = requests.post(url, headers=headers, json=data)

    if response is not None and response.status_code == 200:
        # Установка статуса отправки в True
        message.send_status = True
        message.save()  # Сохранение изменений в объекте message
    else:
        # Обработка случая, когда объект response является
        # None или код состояния не равен 200
        handle_message_error(message, response)

    print(f'response: {response}, message_id: {message.id}, status_code '
          f'{response.status_code}')


def handle_message_error(message, error):
    """Обработчик ошибок при отправке сообщения через сторонний сервер"""
    # Обработка ошибок при отправке сообщений
    # Логирование ошибок
    error_message = str(error)
    # Здесь можно добавить логику для обработки ошибки, например,
    # запись в журнал ошибок или отправку уведомления администратору
    print(f"Ошибка при отправке сообщения {message.id}: {error_message}")
