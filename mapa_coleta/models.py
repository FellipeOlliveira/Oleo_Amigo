from django.db import models
# Create your models here.

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    login = models.CharField(max_length=255, default='', blank=False)
    password = models.CharField(max_length=255)
    adress_latitude = models.FloatField()
    adress_longitude = models.FloatField()
    trash_info = models.JSONField()  # JSONField está disponível a partir do Django 3.1
    trash_section = models.TextField()

    class Meta:
        db_table = 'users'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.login
