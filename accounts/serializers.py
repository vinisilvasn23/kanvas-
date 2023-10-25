from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "email", "password", "is_superuser")
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that username already exists."
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="user with this email already exists."
                    )
                ]
            },
        }

    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        return account
