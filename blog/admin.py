from django.contrib import admin
from .models import Categoria, Autor, Post

#   Importar y Exportar del Administrador de Django
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resources_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'correo']
    list_display = ('nombre', 'apellido', 'correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResource



admin.site.register(Categoria, CategoryAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)