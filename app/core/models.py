from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombres')
    correo = models.EmailField(max_length=254)

    