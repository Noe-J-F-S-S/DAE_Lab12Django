from django.db import models

# Create your models here.
class Autor(models.Model):
     #idAutor = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=100)
     nacionalidad = models.CharField(max_length=50)

class Libro(models.Model):
     #idLibro = models.AutoField(primary_key=True)
     codigo = models.IntegerField(default=0)
     titulo = models.CharField(max_length=100)
     isbn = models.CharField(max_length=30)
     editorial = models.CharField(max_length=60)
     numpags = models.SmallIntegerField()

class Usuario(models.Model):
     #idUsuario = models.AutoField(primary_key=True)
     numUsuario= models.IntegerField(default=0)
     nif = models.CharField(max_length=20)
     nombre = models.CharField(max_length=100)
     direccion =models.CharField(max_length=255)
     telefono = models.IntegerField(30)

class Prestamo(models.Model):
     #idPrestamos = models.AutoField(primary_key=True)
     idLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
     idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     fecPrestamo = models.DateField()
     fecdevolucion = models.DateField()

#########################################################################








