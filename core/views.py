from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.template import loader

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
    # func = Cad_Funcionario.objects.get(id=pk)
    func = get_object_or_404(Cad_Funcionario, id=pk)

    context = {
        'funcionario': func
    }
    return render(request, 'funcionarios.html', context)  

def cliente(request, pk):
    # cli = Cad_Cliente.objects.get(id=pk)
    cli = get_object_or_404(Cad_Funcionario, id=pk)

    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)