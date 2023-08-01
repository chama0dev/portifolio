from rest_framework import serializers

from .models import Tarefas

class TarefaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tarefas 
        fields = '__all__'
