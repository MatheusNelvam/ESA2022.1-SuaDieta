from django.shortcuts import render
from dietas.models import Dieta

# Create your views here.
def index(request):
    dados = {}
    
    dietas = Dieta.objects.all()
    
    dados['dietas'] = dietas
    
    return render(request, 'dietas/index.html', dados)

def teste(request):
    
    
    return render(request, 'dietas/teste.html')