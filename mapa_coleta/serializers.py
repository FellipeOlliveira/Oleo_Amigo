from rest_framework import serializers
from .models import User , Teste_Api , Enderecos_Pontos_Lixo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #Qual o modelo q sera retornado
        fields = '__all__'  # Todos os campos do modelo

class TesteApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste_Api
        fields = '__all__'

class EnderecosPontosLixoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos_Pontos_Lixo
        fields = '__all__'