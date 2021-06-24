from django.shortcuts import render
#   Importar Modelo
from .models import Post, Categoria
#   Retornar un Error 404 Si no se encuentra
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    posts = Post.objects.filter( estado  =   True    )

    return render(request, 'index.html', {
        'posts' : posts
    })


def detailview(request, slug):

    posts = get_object_or_404(Post, slug= slug)
    return render(request, 'post.html', {
        'detailview' : posts
    })


def generales(request):

    posts = Post.objects.filter( 
        estado  =   True, 
        categoria= Categoria.objects.get(nombre__iexact = 'General')  
        )

    return render(request, 'generales.html', {
        'posts' : posts
    })

def programacion(request):

    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Programacion')  
    )

    return render(request, 'programacion.html', {
        'posts' : posts
    })

def videojuegos(request):

    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Videojuegos')  
    )
    return render(request, 'videojuegos.html',  {
        'posts' : posts
    })

def tecnologia(request):
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Tecnologia')  
    )

    return render(request, 'tecnologia.html', {
        'posts' : posts
    })

def tutoriales(request):
    posts = Post.objects.filter( 
    estado  =   True, 
    categoria= Categoria.objects.get(nombre__iexact = 'Tutoriales')  
    )
    return render(request, 'tutoriales.html', {
        'posts' : posts
    })