from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout

from .models import Tarefas
from .formulario import FormularioTarefas

def index_lista_de_tarefas (request):
   if request.user.is_authenticated:
      return redirect("exibir_tarefas")
   return render(request,"lista_de_tarefas/index.html")


def cadastro(request):
   if request.method == "GET":
      return render(request,"lista_de_tarefas/cadastro.html")
   
   elif request.method == "POST":
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')      
      user = User.objects.filter(username = username )
      if user:
         return redirect("logar")
      else :
         user = User.objects.create_user(username=username,password=password)
         #user.save()
         login(request,user)
         return redirect("exibir_tarefas")
   

def logar(request):
   if request.method == "GET":
      return render(request,"lista_de_tarefas/login.html")
   
   elif request.method == "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')

      user = authenticate(username=username, password=password)
      if user is not None:
         login(request,user)
         return redirect("exibir_tarefas")
      else:
         return redirect("cadastro")
      
def logout_view(request):
   logout(request)
   return redirect("index_lista_de_tarefas")

def exibir_tarefas(request) :
   if request.user.is_authenticated:
      tarefas = Tarefas.objects.all()
      username = request.user.username
      context = {"tarefas":tarefas,"username":username}
      return render(request, "lista_de_tarefas/exibir_tarefas.html", context)
   else :
      return redirect("logar")
   
def criar_tarefa(request):
    tarefas = FormularioTarefas()
    username = request.user.username
    context = {"tarefas":tarefas,"username":username}
    
    if request.method == "POST":
        formulario = FormularioTarefas(request.POST)
        if formulario.is_valid():
            #formulario.save()
            return redirect("exibir_tarefas")
        return HttpResponse("Erro")
    else:
        return render(request,'lista_de_tarefas/criar_tarefa.html',context)

def editar_tarefa(request,pk):
    tarefa = Tarefas.objects.get(pk=pk)
    form = FormularioTarefas(request.POST or None,instance=tarefa)
    username = request.user.username
    if form.is_valid():
        #form.save()
        return redirect("exibir_tarefas")
    else:
        print(form.errors)
        return render(request,'lista_de_tarefas/editar_tarefa.html',{'form':form,"username":username})
      
def deletar_tarefa(request,pk):
    tarefa = Tarefas.objects.get(pk=pk)
    form = FormularioTarefas(request.POST or None,instance=tarefa)
    username = request.user.username
    if request.method == "POST":
        tarefa.delete()
        return redirect("exibir_tarefas")
    return render (request,'lista_de_tarefas/deletar_tarefa.html',{'form':form,"username":username})