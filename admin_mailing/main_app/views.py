from rest_framework import generics
from .models import Client, Dispatch, Message
from .serializers import ClientSerializer, DispatchSerializer, MessageSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DispatchListCreateView(generics.ListCreateAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class DispatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer