from django.db import models
from django.contrib.auth.models import User

class TarefaModel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome