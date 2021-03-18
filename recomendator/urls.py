from django.urls import path

#from recomendator.views import *

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('Respuesta/', views.test, name='Respuesta'),
]