from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm


def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all() # managers sao classes que o django implementa para todos o models. e os managers trazem operaçoes de banco de dados
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = reversed(Transacao.objects.all())
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk) # get() retorna apenas 1 objeto, em quanto filter() retornar varios
    form = TransacaoForm(request.POST or None, instance=transacao)
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')



def login(request):
    return render(request, 'contas/login.html')


def register(request):
    return render(request, 'contas/register.html')

 
