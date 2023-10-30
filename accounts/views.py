from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Rota para criação de contas",
    tags=["Criação de usuário"],
)
class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
