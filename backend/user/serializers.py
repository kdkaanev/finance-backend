from rest_framework import serializers

from backend.user.models import FinanceUser, Profile


class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ('email', )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',)
