from dietas.models import Dieta
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    dietas = Dieta.objects.all()
    
    paginator = Paginator(dietas, 3)
    page = request.GET.get('page')
    dietas_per_page = paginator.get_page(page)

    dados = {}
    
    dados['dietas'] = dietas_per_page
    
    return render(request, 'dietas/index.html', dados)

def teste(request):
    
    return render(request, 'dietas/teste.html')