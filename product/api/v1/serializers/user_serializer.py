from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription, Balance

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('user', 'amount')
    
    def update(self, instance, validated_data):
        amount = validated_data.get('amount', instance.amount)
        if amount < 0:
            raise serializers.ValidationError({'amount': 'Баланс не может быть отрицательным.'})
        instance.amount = amount
        instance.save()
        return instance
        

class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    user = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = Subscription
        fields = (
             'id',
            'user',
            'course',
            'subscribed_at'
        )
