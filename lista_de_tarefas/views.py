from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout
from django.views.decorators.http import require_http_methods
from django.contrib import messages


from .models import Tarefas
from .formulario import FormularioTarefas

def index_lista_de_tarefas (request):
   if request.user.is_authenticated:
      return redirect("exibir_tarefas")
   return render(request,"lista_de_tarefas/index.html")

@require_http_methods(["GET","POST"])
def cadastro(request):
   if request.method == "GET":
      return render(request,"lista_de_tarefas/cadastro.html")
   elif request.method == "POST":
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')      
      user = User.objects.filter(username = username )
      if user:
         messages.warning(request,'Voce já tem um cadastro, Voce será redirecionado para a pagina de login')
         return redirect("logar")
      else :
         user = User.objects.create_user(username=username,password=password)
         user.save()
         login(request,user)
         return redirect("exibir_tarefas")
   
@require_http_methods(["GET","POST"])
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
         messages.warning(request,'Voce NÃO possui um cadastro, será redirecionado para a pagina de cadastro ')
         return redirect("cadastro")
      
@require_http_methods(["GET","POST"])
def logout_view(request):
   logout(request)
   messages.success(request,'Volte Sempre !!! ')
   return redirect("index_lista_de_tarefas")

@require_http_methods(["GET","POST"])
def exibir_tarefas(request) :
   if request.user.is_authenticated:
      tarefas = Tarefas.objects.filter(usuario=request.user)
      username = request.user.username
      context = {"tarefas":tarefas,"username":username}
      return render(request, "lista_de_tarefas/exibir_tarefas.html", context)
   else :
      return redirect("logar")

@require_http_methods(["GET","POST"])
def criar_tarefa(request):
    tarefas = FormularioTarefas()
    username = request.user.username
    context = {"tarefas":tarefas,"username":username}
    
    if request.method == "POST":
         formulario = FormularioTarefas(request.POST,user=request.user)
         if formulario.is_valid():
            formulario.save()
            return redirect("exibir_tarefas")
         return HttpResponse( f"{formulario.errors}Invalido !!! Retorne porfavor e corrija o erro")
    else:
        return render(request,'lista_de_tarefas/criar_tarefa.html',context)
    
@require_http_methods(["GET","POST","PATCH"])
def editar_tarefa(request,pk):
   tarefa = Tarefas.objects.get(pk=pk,usuario=request.user)
   form = FormularioTarefas(request.POST or None,instance=tarefa)
   username = request.user.username
   if request.method == "POST":
      if form.is_valid():
         tarefa = form.save(commit=False)
         tarefa.usuario = request.user
         tarefa.save()
         return redirect("exibir_tarefas")
      return HttpResponse( f"{form.errors}Invalido !!! Retorne porfavor e corrija o erro")
   else:
      return render(request,'lista_de_tarefas/editar_tarefa.html',{'form':form,"username":username})
    
@require_http_methods(["GET","POST","DELETE"])
def deletar_tarefa(request,pk):
    tarefa = Tarefas.objects.get(pk=pk,usuario=request.user)
    form = FormularioTarefas(request.POST or None,instance=tarefa)
    username = request.user.username
    if request.method == "POST":
        tarefa.delete()
        return redirect("exibir_tarefas")
    return render (request,'lista_de_tarefas/deletar_tarefa.html',{'form':form,"username":username})