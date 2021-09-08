from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import CrearRegistro
from getecoapp.models import Ciudad
# Create your views here.

@api_view(['GET', 'POST'])
def crear_registro(request):
    if "GET" == request.method:
        form = CrearRegistro()
        return render(request, './crear_regristro.html', {'form': form})
