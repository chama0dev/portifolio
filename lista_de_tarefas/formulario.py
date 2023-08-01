from django import forms
from .models import Tarefas

class FormularioTarefas(forms.ModelForm):
    class Meta :
        model = Tarefas
        fields = ('titulo','descricao')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FormularioTarefas, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(FormularioTarefas, self).save(commit=False)
        instance.usuario = self.user
        if commit:
            instance.save()
        return instance