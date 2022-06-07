from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from productos.models import *
from productos.forms import *

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

#Productos
def producto_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos.html', context = context)

class CrearProducto(CreateView):
    model = Producto
    template_name = 'crear_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})  

class DetalleProducto(DetailView):
    model = Producto
    template_name= 'detalle_producto.html'

class ActualizarProducto(UpdateView):
    model = Producto
    template_name = 'actualizar_producto.html'
    fields = ['name', 'descripcion', 'precio', 'activo']

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'

    def get_success_url(self):
        return reverse('productos')

#Categorias
def categoria_view(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categorias.html', context = context)

class CrearCategoria(CreateView):
    model = Categoria
    template_name = 'crear_categoria.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_categoria', kwargs = {'pk':self.object.pk})  

class DetalleCategoria(DetailView):
    model = Categoria
    template_name= 'detalle_categoria.html'

class ActualizarCategoria(UpdateView):
    model = Categoria
    template_name = 'actualizar_categoria.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('detalle_categoria', kwargs = {'pk':self.object.pk})

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'eliminar_categoria.html'

    def get_success_url(self):
        return reverse('categorias')

#Locales
def local_view(request):
    locales = Local.objects.all()
    context = {'locales': locales}
    return render(request, 'locales.html', context = context)

def crear_producto(request):
    if request.method == 'GET':
        form = product_form
        context = {'form':form}
        return render(request, 'crear_producto.html', context = context)
    else:
        form = product_form(request.POST)
        if form.is_valid():
            new_product = Producto.objects.create(
                name = form.cleaned_data['name'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
                SKU = form.cleaned_data['SKU'],
                activo = form.cleaned_data['activo'],
            )
            context = {'new_product':new_product}
        return render(request, 'crear_producto.html', context = context)

def search_product_view(request):
    products = Producto.objects.filter(name = request.GET["search"])
    context = {"products":products}
    return render(request, "search_product.html", context = context)
class CrearLocal(CreateView):
    model = Local
    template_name = 'crear_local.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_local', kwargs = {'pk':self.object.pk})  

class DetalleLocal(DetailView):
    model = Local
    template_name= 'detalle_local.html'

class ActualizarLocal(UpdateView):
    model = Local
    template_name = 'actualizar_local.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('detalle_local', kwargs = {'pk':self.object.pk})

class EliminarLocal(DeleteView):
    model = Local
    template_name = 'eliminar_local.html'

    def get_success_url(self):
        return reverse('locales')
