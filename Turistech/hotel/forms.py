from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Asegúrate de importar tu modelo de usuario personalizado correctamente
UsuarioHotel = get_user_model()

class UsuarioHotelRegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioHotel
        # Especifica los campos que quieres incluir en tu formulario
        fields = ('username', 'email', 'password1', 'password2', 'tipo', 'direccion', 'descripcion')

    # Opcional: Puedes agregar validaciones adicionales o lógica de inicialización aquí
