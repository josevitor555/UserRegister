from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar os dados inseridos no banco de dados
    new_user = Usuario()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()
    # nome = request.POST.get('nome')
    # idade = request.POST.get('idade')
    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)