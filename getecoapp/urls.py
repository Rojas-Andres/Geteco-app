from django.urls import path
from getecoapp.views import crear_registro
urlpatterns = [
    path('crear/', crear_registro, name='crear_registro'),

] 