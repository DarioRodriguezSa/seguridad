
from django.contrib import admin
from django.urls import path
from django.conf import settings

from inicio.views import HomePageView
from miembros import views as views_m
from actividades import views as views_a
from eventos import views as views_e
from gastos import views as views_g

urlpatterns = [

    path('', HomePageView.as_view(), name="home"),



#-------------------------------MIEMBROS
    path('miembros/', views_m.agregar_miembro, name="agregar_miembro"),
    path('listar_miembros/', views_m.listar_miembros, name="listar_miembros"),



#------------------------------ACTIVIDADES
    path('actividades/', views_a.actividades, name="actividades"),



#--------------------------------EVENTOS
    path('eventos/', views_e.eventos, name="eventos"),




#---------------------------------GASTOS
    path('gastos/', views_g.gastos, name="gastos"),
    




    path('admin/', admin.site.urls), 
]

