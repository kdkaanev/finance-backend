from rest_framework import serializers

from backend.user.models import FinanceUser


class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ('email', )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ('email', 'first_name', 'last_name', 'date_joined', 'last_login')
        read_only_fields = ('email', 'date_joined', 'last_login')