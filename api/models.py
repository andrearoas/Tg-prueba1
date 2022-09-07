from django.db import models


# Create your models here.

class User(models.Model):
    nombre_user = models.CharField(max_length=30)
    apellido_user = models.CharField(max_length=30)
    correo_user = models.EmailField(max_length=50)
    contraseña_user = models.CharField(max_length=30)


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    tipo_categoria = models.CharField(max_length=1)


class Cultivo(models.Model):
    foto_culti = models.ImageField(upload_to='api')
    nombre_culti = models.CharField(max_length=30)
    nombre_scie_culti = models.CharField(max_length=30)
    descripcion_culti = models.TextField(max_length=600)
    tiempo_germinacion = models.IntegerField()
    tiempo_cosecha = models.IntegerField()
    tiempo_siembra = models.CharField(max_length=15)
    tiempo_sol_culti = models.CharField(max_length=20)
    cantidad_riego_culti = models.CharField(max_length=30)
    distancia_plantas = models.IntegerField()
    altura_max_culti = models.IntegerField()
    tipo_recipiente = models.CharField(max_length=30)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

