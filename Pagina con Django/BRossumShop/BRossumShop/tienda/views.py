from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

def producto(request):
    return render(request, 'tienda/producto.html')

def acercade(request):
    return render(request, 'tienda/acercade.html')

def perfil(request):
    return render(request, 'tienda/perfil.html')

def inicio_sesion(request):
    return render(request, 'tienda/Inicio_Sesion.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save(

                user = authenticate(nombre=user_creation_form.cleaned_data['nombre'],contraseña=user_creation_form.cleaned_data['contraseña'])
            )
    return render(request, 'tienda/Registro.html')
