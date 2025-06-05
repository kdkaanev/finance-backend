from rest_framework import serializers

from backend.user.models import FinanceUser


class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ('email', )