from django.urls import path
from app_cadastroUsuario import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('usuarios/', views.usuarios, name="listagem_usuarios")
]
