from rest_framework import generics
from .models import Client, Dispatch, Message
from .serializers import ClientSerializer, DispatchSerializer, \
    MessageSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import MessageFilter, ClientFilter, DispatchFilter

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
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientLimitOffsetPagination
    filterset_class = ClientFilter

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class DispatchListCreateView(generics.ListCreateAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    pagination_class = DispatchLimitOffsetPagination
    filterset_class = DispatchFilter


class DispatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessageLimitOffsetPagination
    filterset_class = MessageFilter


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
