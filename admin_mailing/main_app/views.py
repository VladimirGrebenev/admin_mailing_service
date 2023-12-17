from rest_framework import generics
from .models import Client, Dispatch, Message
from .serializers import ClientSerializer, DispatchSerializer, \
    MessageSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import MessageFilter, ClientFilter, DispatchFilter
from drf_yasg.utils import swagger_auto_schema


# пагинатор для Client
class ClientLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


# пагинатор для Dispatch
class DispatchLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


# пагинатор для Message
class MessageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ClientListCreateView(generics.ListCreateAPIView):
    """List all Clients or create new Client"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientLimitOffsetPagination
    filterset_class = ClientFilter


class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """By client uu_id, you can retrieve, update or patch, delete client"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DispatchListCreateView(generics.ListCreateAPIView):
    """List all Dispatches or create new Dispatch"""
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    pagination_class = DispatchLimitOffsetPagination
    filterset_class = DispatchFilter


class DispatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """By dispatch uu_id, you can retrieve, update or patch, delete dispatch"""
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    """List all Messages or create new Message"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessageLimitOffsetPagination
    filterset_class = MessageFilter


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """By message uu_id, you can retrieve, update or patch, delete message"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
