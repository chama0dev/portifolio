from django.shortcuts import render,redirect
from django.http import response,HttpResponse



from portifolio.formularios import FormularioCadastro

def index (request):
    form = FormularioCadastro()
    return render (request=request,template_name="portifolio/index.html",context={"form":form})

def processa_formulario(resquest):
    formulario = FormularioCadastro(resquest.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect("index_portifolio")
    return HttpResponse( f"{formulario.errors} ERRO !!! Não foi possivel enviar o formulario, Retorne e reenvie por favor.")
    