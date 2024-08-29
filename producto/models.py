from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/', null=True,verbose_name='Imagen')
    precio = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Precio')
    descripcion = models.TextField(verbose_name='Descripcion',null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None,keep_parents=False):
        # Este metodo se ejecuta cuando se elimina un objeto de la base de datos
        # En este caso, se puede agregar codigo para manejar la eliminacion de la imagen asociada al producto
        self.imagen.storage.delete(self.imagen.name)
        # Eliminar imagen asociada
        super().delete()