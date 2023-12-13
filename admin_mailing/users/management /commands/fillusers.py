from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        # добавляем тестовых пользователей
        test_users_list = []
        CustomUser.objects.filter(email__startswith='test').delete()
        for i in range(3):
            CustomUser.objects.create_user(
                first_name=f'first name {i}',
                last_name=f'last name {i}',
                user_name=f'user{i}',
                email=f'test_mail{i}@mail.ru',
                password=f'pass{i}'
            )

        # добавляем тестового админа superuser
        CustomUser.objects.filter(email='admin@mail.ru').delete()
        CustomUser.objects.create_superuser('admin@mail.ru', 'admin',
                                            user_name='admin')
