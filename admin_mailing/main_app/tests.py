import json
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import (APIRequestFactory, force_authenticate,
                                 APIClient, APISimpleTestCase, APITestCase)
from mixer.backend.django import mixer
from .models import Client, Dispatch, Message
from users.models import CustomUser
from .views import (ClientListCreateView, ClientRetrieveUpdateDestroyView,
                    DispatchListCreateView, DispatchRetrieveUpdateDestroyView,
                    MessageListCreateView, MessageRetrieveUpdateDestroyView)


# Create your tests here.

class TestClientListCreateView(TestCase):
    def test_get_clients_list_auth_user(self):
        """ Пробуем получить доступ к списку клиентов авторизованным
        пользователем """
        factory = APIRequestFactory()
        request = factory.get('/clients/')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_clients_list_guest(self):
        """ Пробуем получить доступ к списку клиентов не авторизованным
        пользователем """
        factory = APIRequestFactory()
        request = factory.get('/clients/')
        view = ClientListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_client_auth_user(self):
        """ Пробуем создать клиента авторизованным пользователем """
        factory = APIRequestFactory()
        data = {
            'phone_number': '79834578640',
            'operator_code': '983',
            'tag': 'mts',
            'timezone': 'GMT+03'
        }
        request = factory.post('/clients/', data=data, format='json')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_client_guest(self):
        """ Пробуем создать клиента не авторизованным пользователем """
        factory = APIRequestFactory()
        data = {
            'phone_number': '79834578640',
            'operator_code': '983',
            'tag': 'mts',
            'timezone': 'GMT+03'
        }
        request = factory.post('/clients/', data=data, format='json')
        view = ClientListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_client_auth_user_incomplete_data(self):
        """ Пробуем создать клиента с неполными данными """
        factory = APIRequestFactory()
        data = {
            'phone_number': '79834578640',
            'operator_code': '983',
            'tag': 'mts',
            # 'timezone': 'GMT+03' incomplete data
        }
        request = factory.post('/clients/', data=data, format='json')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestClientRetrieveUpdateDestroyView(TestCase):
    def test_get_client_detail_auth_user(self):
        """ Пробуем получить данные клиента авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        request = factory.get(f'/clients/{client.uu_id}/')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_client_detail_guest(self):
        """ Пробуем получить данные клиента не авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        request = factory.get(f'/clients/{client.uu_id}/')
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_edit_client_auth_user(self):
        """ Редактируем данные клиента авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        new_data = {
            'phone_number': '79834578640',
            'operator_code': '983',
            'tag': 'yota',
            'timezone': 'GMT+01'
        }

        url = reverse('client-retrieve-update-destroy',
                      kwargs={'pk': client.pk})
        request = factory.patch(url, data=new_data, format='json')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_client_guest(self):
        """ Редактируем данные клиента не авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        new_data = {
            'phone_number': '79834578640',
            'operator_code': '983',
            'tag': 'yota',
            'timezone': 'GMT+01'
        }

        url = reverse('client-retrieve-update-destroy',
                      kwargs={'pk': client.pk})
        request = factory.patch(url, data=new_data, format='json')
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_client_auth_user(self):
        """ Удаляем клиента авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        request = factory.delete(f'/clients/{client.uu_id}/')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_client_guest(self):
        """ Удаляем клиента авторизованным пользователем """
        factory = APIRequestFactory()
        client = mixer.blend(Client, phone_number='79834578640',
                             operator_code='983', tag='mts', timezone='GMT+03')
        request = factory.delete(f'/clients/{client.uu_id}/')
        view = ClientRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=client.pk)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestMessageListCreateView(TestCase):
    def test_get_messages_list_auth_user(self):
        """ Пробуем получить доступ к списку сообщений авторизованным
        пользователем """
        factory = APIRequestFactory()
        request = factory.get('/messages/')
        # авторизуемся, чтобы получить доступ
        custom_user = CustomUser.objects.create_user(
            'doomguy@mail.ru', 'iddqd', )
        force_authenticate(request, custom_user)
        view = MessageListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_messages_list_guest(self):
        """ Пробуем получить доступ к списку сообщений не авторизованным
        пользователем """
        factory = APIRequestFactory()
        request = factory.get('/messages/')
        view = MessageListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# # !!! Тесты по Dispatch работают только при запущенном celery + redis
# class TestDispatchListCreateView(TestCase):
#     def test_get_dispatches_list_auth_user(self):
#         """ Пробуем получить доступ к списку рассылок авторизованным
#         пользователем """
#         factory = APIRequestFactory()
#         request = factory.get('/dispatches/')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_dispatches_list_guest(self):
#         """ Пробуем получить доступ к списку рассылок не авторизованным
#         пользователем """
#         factory = APIRequestFactory()
#         request = factory.get('/dispatches/')
#         view = DispatchListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_create_dispatch_auth_user(self):
#         """ Пробуем создать рассылку авторизованным пользователем """
#         factory = APIRequestFactory()
#         data = {
#             "start_datetime": "4100-12-16T10:12",
#             "end_datetime": "4105-12-16T10:12",
#             "message_text": "come get some",
#             "tag_filter": "new_tag",
#             "operator_code_filter": "983"
#         }
#         request = factory.post('/dispatches/', data=data, format='json')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_create_dispatch_guest(self):
#         """ Пробуем создать рассылку не авторизованным пользователем """
#         factory = APIRequestFactory()
#         data = {
#             "start_datetime": "4100-12-16T10:12",
#             "end_datetime": "4105-12-16T10:12",
#             "message_text": "come get some",
#             "tag_filter": "new_tag",
#             "operator_code_filter": "983"
#         }
#         request = factory.post('/dispatches/', data=data, format='json')
#         view = DispatchListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_create_dispatch_auth_user_incomplete_data(self):
#         """ Пробуем создать клиента с неполными данными """
#         factory = APIRequestFactory()
#         data = {
#             "start_datetime": "4100-12-16T10:12",
#             # "end_datetime": "4105-12-16T10:12", incomplete_data
#             "message_text": "come get some",
#             "tag_filter": "new_tag",
#             "operator_code_filter": "983"
#         }
#         request = factory.post('/dispatches/', data=data, format='json')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
# # !!! Тесты по Dispatch работают только при запущенном celery + redis
# class TestDispatchRetrieveUpdateDestroyView(TestCase):
#     def test_get_dispatch_detail_auth_user(self):
#         """ Пробуем получить данные рассылки авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         request = factory.get(f'/dispatches/{dispatch.uu_id}/')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_dispatch_detail_guest(self):
#         """ Получаем данные рассылки не авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         request = factory.get(f'/dispatches/{dispatch.uu_id}/')
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_edit_dispatch_auth_user(self):
#         """ Редактируем данные рассылки авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         new_data = {
#             "start_datetime": "4100-12-16T10:12",
#             "end_datetime": "4105-12-16T10:12",
#             "message_text": "come get some",
#             "tag_filter": "new_tag",
#             "operator_code_filter": "983"
#         }
#
#         url = reverse('dispatch-retrieve-update-destroy',
#                       kwargs={'pk': dispatch.pk})
#         request = factory.patch(url, data=new_data, format='json')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_edit_dispatch_guest(self):
#         """ Редактируем данные рассылки не авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         new_data = {
#             "start_datetime": "4100-12-16T10:12",
#             "end_datetime": "4105-12-16T10:12",
#             "message_text": "come get some",
#             "tag_filter": "new_tag",
#             "operator_code_filter": "983"
#         }
#
#         url = reverse('dispatch-retrieve-update-destroy',
#                       kwargs={'pk': dispatch.pk})
#         request = factory.patch(url, data=new_data, format='json')
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_delete_dispatch_auth_user(self):
#         """ Удаляем рассылку авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         request = factory.delete(f'/dispatches/{dispatch.uu_id}/')
#         # авторизуемся, чтобы получить доступ
#         custom_user = CustomUser.objects.create_user(
#             'doomguy@mail.ru', 'iddqd', )
#         force_authenticate(request, custom_user)
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_delete_dispatch_guest(self):
#         """ Удаляем рассылку авторизованным пользователем """
#         factory = APIRequestFactory()
#         dispatch = mixer.blend(Dispatch, start_datetime="4100-12-16T10:12",
#                                end_datetime="4105-12-16T10:12",
#                                message_text="come get some",
#                                tag_filter="new_tag",
#                                operator_code_filter="983")
#         request = factory.delete(f'/dispatches/{dispatch.uu_id}/')
#         view = DispatchRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=dispatch.pk)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
