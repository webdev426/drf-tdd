from django.contrib.auth.models import User

from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, )

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined", "password", "confirm_password")

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return super(UserRegistrationSerializer, self).create(validated_data)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return attrs
