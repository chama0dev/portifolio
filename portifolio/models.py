from django.db import models


class Formulario(models.Model):
    nome=models.CharField(max_length=50, blank=False)
    email=models.EmailField(max_length=254,blank=False)
    mensagem=models.TextField(max_length=1000,blank=False)

    def __str__(self) -> str:
        return self.nome