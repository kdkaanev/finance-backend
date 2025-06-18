from rest_framework import serializers

from backend.user.models import FinanceUser, Profile


class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ('email', )

    def validate_email(self, value):
        """
        Check that the email is not already in use.
        """
        if FinanceUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def create(self, validated_data):
        """
        Create a new FinanceUser instance.
        """
        user = FinanceUser.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',)
