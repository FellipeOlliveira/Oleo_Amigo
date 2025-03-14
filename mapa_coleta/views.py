from rest_framework.exceptions import NotFound

from rest_framework import generics
from .models import User , Teste_Api , Enderecos_Pontos_Lixo
from .serializers import UserSerializer , TesteApiSerializer , EnderecosPontosLixoSerializer


# Lista os usuarios e cria um novo
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# CRUD basico(precisa do id do usuario)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self):
        try:
            return super().get_object()
        except User.DoesNotExist:
            raise NotFound("Usuário não encontrado")

#TESTE API
class TesteApiListCreateView(generics.ListCreateAPIView):
    queryset = Teste_Api.objects.all()
    serializer_class = TesteApiSerializer

class TesteApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teste_Api.objects.all()
    serializer_class = TesteApiSerializer


#Endereços dos pontos de coleta
class EnderecoListCreateView(generics.ListCreateAPIView):
    queryset = Enderecos_Pontos_Lixo.objects.all()
    serializer_class = EnderecosPontosLixoSerializer

# CRUD básico (Requer ID do endereço)
class EnderecoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enderecos_Pontos_Lixo.objects.all()
    serializer_class = EnderecosPontosLixoSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Enderecos_Pontos_Lixo.DoesNotExist:
            raise NotFound("Endereço não encontrado")