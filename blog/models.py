from django.db import models

# Create your models here.

class Categoria (models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null= False, blank=False)
    estado = models.BooleanField('Estado la publicacion Activo/No Activo', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creacion', auto_created=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor (models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Autor', max_length=200, null= False, blank=False)
    apellido = models.CharField('Apellido de Autor', max_length=200, null= False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    paginaweb = models.URLField('Pagina Web', null=True, blank=True)
    correo = models.EmailField('Correo Electronico', null=False, blank=False)
    estado = models.BooleanField('Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creacion', auto_created=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return  '{0}, {1}'.format(self.apellido, self.nombre)
