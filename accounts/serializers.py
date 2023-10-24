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
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                    )
                ]
            },
        }
