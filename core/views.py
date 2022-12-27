from django.shortcuts import render

def index(request):
    context = {
        'apresentacao': 'A melhor clinica de Curitiba!',
        'divulgacao': 'Venha fazer seu tratemento aqui!'
    }
    return render(request, 'index.html', context)

def funcionarios(request):
    return render(request, 'funcionarios.html')    
