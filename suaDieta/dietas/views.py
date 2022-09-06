from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dietas/index.html')

def teste(request):
    return render(request, 'dietas/teste.html')