
# Create your models here.
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def str(self):
        return f"{self.nombre} {self.apellido}"

class Nota(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def str(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    Nota = models.ForeignKey(Nota, on_delete=models.CASCADE)

    def str(self):
        return f"{self.nombre} {self.apellido}"