from django.shortcuts import render

from .models import Cad_Funcionario, Cad_Cliente

def index(request):
    funcionarios = Cad_Funcionario.objects.all()
    clientes = Cad_Cliente.objects.all()
    context = {
        'apresentacao': 'A melhor clinica de Curitiba!',
        'divulgacao': 'Venha fazer seu tratemento aqui!',
        'funcionarios': funcionarios,
        'clientes': clientes,
    }
    return render(request, 'index.html', context)

def funcionario(request, pk):
    func = Cad_Funcionario.objects.get(id=pk)

    context = {
        'funcionario': func
    }
    return render(request, 'funcionarios.html')  

def cliente(request, pk):
    cli = Cad_Cliente.objects.get(id=pk)

    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html')
