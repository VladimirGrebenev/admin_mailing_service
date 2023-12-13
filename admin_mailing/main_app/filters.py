from django_filters import rest_framework as filters, DateFromToRangeFilter
from .models import Client, Dispatch, Message


class ClientFilter(filters.FilterSet):
    phone_number = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Client
        fields = ['phone_number']


class DispatchFilter(filters.FilterSet):
    start_datetime = DateFromToRangeFilter()

    class Meta:
        model = Dispatch
        fields = ['start_datetime']


class MessageFilter(filters.FilterSet):
    created_datetime = DateFromToRangeFilter()

    class Meta:
        model = Message
        fields = ['dispatch', 'created_datetime']
