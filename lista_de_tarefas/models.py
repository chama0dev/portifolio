from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    titulo = models.CharField(max_length=50, error_messages="Erro : O maximo de caracter é 50")
    descricao = models.TextField(blank=True, max_length=200 , error_messages="Erro : O maximo de caracter é 200")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo 