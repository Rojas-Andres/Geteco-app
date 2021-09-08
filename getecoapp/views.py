from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

def Index(request):
    return render(request, 
        './index.html'
        , {})
@api_view(['GET', 'POST'])
def crear_registro(request):
    if "GET" == request.method:
        
        return render(request, './crear_regristro.html')