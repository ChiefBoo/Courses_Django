from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from users.models import Balance
from api.v1.serializers.user_serializer import BalanceSerializer
from rest_framework.permissions import IsAdminUser

from api.v1.serializers.user_serializer import CustomUserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)
    

class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [IsAdminUser]
