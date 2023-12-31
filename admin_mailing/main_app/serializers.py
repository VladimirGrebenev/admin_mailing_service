from rest_framework import serializers
from .models import Client, Dispatch, Message
from datetime import datetime, timedelta
from django.utils import timezone


class ClientSerializer(serializers.ModelSerializer):
    """Сериалайзер класса Клиент"""

    class Meta:
        model = Client
        fields = '__all__'


class DispatchSerializer(serializers.ModelSerializer):
    """Сериалайзер класса Рассылка, имеет дополнительную валидацию полей
    времени старта и финиша рассылки"""
    start_datetime = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M", ],
        help_text=("Введите дату и время старта в формате 'YYYY-MM-DD HH:MM'")
    )
    end_datetime = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M", ],
        help_text=("Введите дату и время финиша в формате 'YYYY-MM-DD HH:MM'")
    )

    def validate(self, data):
        """Дополнительная валидация полей старта и финиша Рассылки"""
        if data['start_datetime'] > data['end_datetime']:
            raise serializers.ValidationError("finish must occur after start")
        if data['end_datetime'] <= datetime.now(timezone.utc) + timedelta(
                minutes=5):
            raise serializers.ValidationError(
                "Минимальное время финиша должно быть больше текущего времени "
                "на 5 минут.")
        if data['end_datetime'] <= data['start_datetime'] + timedelta(
                minutes=5):
            raise serializers.ValidationError(
                "Интервал между стартом и финишем должен быть не меньше 5 "
                "минут.")
        return data

    class Meta:
        model = Dispatch
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """Сериалайзер для класса Сообщения"""

    class Meta:
        model = Message
        fields = '__all__'
