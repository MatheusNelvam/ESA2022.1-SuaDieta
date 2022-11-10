# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dietas.models import Dieta



# Create your views here.
def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        # Validando se o nome é null
        if not nome.strip():
            messages.error(request,"O nome não pode ficar em branco")
            return redirect('cadastro')
        
        # Validando se o campo de email não esta em branco
        if not nome.strip():
            messages.error(request,"O campo email não pode ficar em branco")
            return redirect('cadastro')
            
        # Validando senha
        if senha != senha2:
            messages.error(request, "As senhas não são iguais!")
            return redirect('cadastro')
        
        # Verificar se o usuário que queremos criar está na base de dados
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        
        
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if not email.strip():
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect('login')
        
        if not senha.strip():
            messages.error(request, "Senha vazia!")
            return redirect('login')
        
        # Trazendo as informações desse usuário apartir do email
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return render(request, 'dietas/index.html')
            else:
                messages.error(request, 'Credenciais invalidas!.')
                return redirect('login')
        else:
                messages.error(request, 'Credenciais invalidas!.')
                return redirect('login')    
    else:
        if not request.user.is_authenticated:
            return render(request, 'usuarios/login.html')
        else:
            messages.error(request, 'Você já está logado! Por favor efetue o logout.')
            return redirect('index')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!.')
    return redirect('index')

@login_required
def dashboard(request):
    id = request.user.id
    
    dietas = Dieta.objects.order_by('data_inicio').filter(pessoa=id)
    
    paginator = Paginator(dietas, 3)
    page = request.GET.get('page')
    dietas_per_page = paginator.get_page(page)

    dados = {}
    
    dados['dietas'] = dietas_per_page
    
    # print(dados)
    
    return render(request, 'usuarios/dashboard.html', dados)
