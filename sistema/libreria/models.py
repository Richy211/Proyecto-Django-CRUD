from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulos = models.CharField(max_length=100, verbose_name='Titulos')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    
    def __str_(self):
        fila ="Titulo: " + self.titulo + " - " + "Descripción:" + self.descripcion 
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
        
