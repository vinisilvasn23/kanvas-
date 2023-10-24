from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView


class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
