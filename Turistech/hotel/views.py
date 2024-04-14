from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UsuarioHotelRegistroForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redireccionar según el tipo de usuario
            if hasattr(user, 'usuarioshotel'):
                return redirect('/ruta-para-usuariohotel/')
            else:
                return redirect('/ruta-para-usuarios/')
        else:
            # Mensaje de error si la autenticación falla
            return render(request, 'hoteles/login.html', {'error': 'Nombre de usuario o contraseña inválidos.'})
    else:
        return render(request, 'hoteles/login.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                validate_password(password1)
                user = User.objects.create_user(username, email, password1)
                user.save()
                login(request, user)  # Opcional: Inicia sesión automáticamente al usuario
                return redirect('/home/')
            except ValidationError as e:
                return render(request, 'register.html', {'error': e.messages})
            except Exception as e:
                return render(request, 'register.html', {'error': str(e)})
        else:
            return render(request, 'hoteles/register.html', {'error': 'Las contraseñas no coinciden'})

    return render(request, 'hoteles/register.html')