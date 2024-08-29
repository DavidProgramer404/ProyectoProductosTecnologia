from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .form import ProductoForm


# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")


def nosotros(request):
    return render(request, "paginas/nosotros.html")

# contactos

def contactos(request):
    return render(request, "paginas/contactos.html")


def index(request):
    return render(request, "tecnologias/index.html")


# tecnología
def tecnologia(request):
    productos = Producto.objects.all()
    # print(productos)
    return render(request, "tecnologias/index.html", {"productos": productos})


# crear producto
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("tecnologia")
    return render(request, "tecnologias/crear.html", {"formulario": formulario})


def editar(request,id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("tecnologia")
    return render(request, 'tecnologias/editar.html', {"formulario": formulario})


def eliminar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("tecnologias")
