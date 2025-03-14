from django.db import models

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    login = models.CharField(max_length=255, default='', blank=False)
    password = models.CharField(max_length=255)
    adress_latitude = models.FloatField()
    adress_longitude = models.FloatField()
    trash_info = models.JSONField()
    trash_section = models.TextField()

    class Meta:
        db_table = 'users'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.login

class Teste_Api(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    numero_teste = models.TextField(blank=True)
    nome = models.TextField(blank=True)

    class Meta:
        db_table = 'Teste_API_'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome

class Enderecos_Pontos_Lixo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    endereco = models.TextField(blank=True,null=False)
    tipo_lixeira = models.TextField(blank=True,null=True)
    tipo_lixo = models.TextField(blank=True,null=False)
    latitude = models.FloatField()
    longetude = models.FloatField()


    class Meta:
        db_table = 'endereco_pontos_lixo'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.endereco