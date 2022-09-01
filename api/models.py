from django.db import models


# Create your models here.

class User(models.Model):
    nombre_user = models.CharField(max_length=30)
    apellido_user = models.CharField(max_length=30)
    correo_user = models.CharField(max_length=50)
    contraseña_user = models.CharField(max_length=30)
