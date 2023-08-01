"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from portifolio.urls import urlpatterns as urls_portifolio
from lista_de_tarefas.urls import urlpatterns as urls_lista_de_tarefas
from imobiliaria.urls import urlpatterns as urls_imobiliaria
from restaurante.urls import urlpatterns as urls_restaurante




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_portifolio)),
    path('lista_de_tarefas/',include(urls_lista_de_tarefas)),
    path('imobiliaria/',include(urls_imobiliaria)),
    path('restaurante/',include(urls_restaurante)),
]
