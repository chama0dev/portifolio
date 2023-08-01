from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_lista_de_tarefas,name="index_lista_de_tarefas"),
    path('cadastro/',views.cadastro,name="cadastro"),
    path('logar/',views.logar,name="logar"),
    path('exibir_tarefas/',views.exibir_tarefas,name="exibir_tarefas"),
    path("criar_tarefa/",views.criar_tarefa,name='criar_tarefa'),
    path("editar_tarefa/<int:pk>",views.editar_tarefa, name="editar_tarefa"),
    path("deletar_tarefa/<int:pk>",views.deletar_tarefa, name="deletar_tarefa"),
    path("logout",views.logout_view, name="logout_view"),
]
