#   Renderizar Templates
from django.shortcuts import render
#   Importar Modelo
from .models import Post, Categoria
#   Retornar un Error 404 Si no se encuentra
from django.shortcuts import get_object_or_404
#   Fucionalidad Q
from django.db.models import Q
#   Paginacion de Django
from django.core.paginator import Paginator





# Create your views here.
def home(request):

    #   Barra de Busqueda
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( estado  =   True    )

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()


    #Paginator
        #   Contenido de la lista y Numero de Objetos por Pagina
    paginator = Paginator(posts, 2)
    page = request.GET.get('Page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {
        'posts' : posts
    })


def detailview(request, slug):

    posts = get_object_or_404(Post, slug= slug)
    return render(request, 'post.html', {
        'detailview' : posts
    })


def generales(request):
    #   Barra de Busqueda
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( 
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'General')  
        )
    
    if queryset:
        posts = Post.objects.filter(

            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado  =   True, 
            categoria= Categoria.objects.get(nombre__iexact = 'General') 

        ).distinct()

    return render(request, 'generales.html', {
        'posts' : posts
    })

def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Programacion')  
    )

    if queryset:
        posts = Post.objects.filter(

        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset),
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'Programacion') 

        ).distinct()

    return render(request, 'programacion.html', {
        'posts' : posts
    })

def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Videojuegos')  
    )

    if queryset:
        posts = Post.objects.filter(

        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset),
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'Videojuegos') 

        ).distinct()

    return render(request, 'videojuegos.html',  {
        'posts' : posts
    })

def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Tecnologia')  
    )

    if queryset:
        posts = Post.objects.filter(

        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset),
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'Tecnologia') 

        ).distinct()

    return render(request, 'tecnologia.html', {
        'posts' : posts
    })

def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Tutoriales')  
    )
    if queryset:
        posts = Post.objects.filter(

        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset),
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'Tutoriales') 

        ).distinct()
        
    return render(request, 'tutoriales.html', {
        'posts' : posts
    })