from dietas.models import Dieta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dietas.forms import dietaform


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


    

def forms(request):
    context = {}

    user  = get_object_or_404(User, pk=request.user.id)
    form = dietaform(request.POST or None, initial={'pessoa': user})


    if form.is_valid():
        form.save()
        return redirect('index')

    context["form"] = form  
    context["user"] = user

    return render(request, "dietas/forms.html", context)   
     