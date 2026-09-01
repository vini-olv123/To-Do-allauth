from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required
def tarefas_home(request):
    tarefas = TarefaModel.objects.filter(usuario=request.user)
    total = tarefas.count()
    concluidas = tarefas.filter(completo=True).count()

    contexto = {
        "nome": request.user.username,
        "tarefas": tarefas,
        "total": total,
        "concluidas": concluidas
    }
    return render(request, 'tarefas/home.html', contexto)

@login_required
def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            tarefa = formulario.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect("tarefas:home")

    contexto = {
        "form":TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)

@login_required
def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('tarefas:home')

@login_required
def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id, usuario=request.user)
    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    formulario = TarefaForm(instance=tarefa)

    context = {
        'form':formulario
    }
    return render(request, 'tarefas/editar.html', context)