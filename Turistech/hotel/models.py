from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class UsuarioHotel(AbstractUser):
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField()
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="usuariohotel_groups",  # Otro nombre único para el related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuariohotel_user_permissions",  # Otro nombre único para el related_name
        related_query_name="user",
    )
