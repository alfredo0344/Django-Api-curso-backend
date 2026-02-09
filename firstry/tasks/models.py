from django.db import models
# Create your models here.

class Task(models.Model):
  #ChardField es para textos cortos 
  #max_length es para definir la longitud maxima del texto
   title = models.CharField(max_length=200)
   #TextField es para textos largos
   #blank es para que el campo pueda estar vacio
   #null es para que el campo pueda ser nulo
   description = models.TextField(blank=True, null=True)
   
   #BooleanField es para campos de verdadero o falso
   #default es para que el campo tenga un valor por defecto
   completed = models.BooleanField(default=False)
   
   #DateTimeField es para campos de fecha y hora
   #auto_now_add es para que el campo se llene automaticamente con la fecha y hora de creacion
   created_at = models.DateTimeField(auto_now_add=True)
   
   def __str__(self): # type: ignore
     #Retorna el titulo y la descripcion de la tarea
     return  f"{self.title} - {self.completed}"