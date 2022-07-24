from msilib.schema import Class
from multiprocessing import context
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """Vista que carga la página de inicio"""
    template_name = "inicio.html"

# 1.- lista todos lo empleados de la empresa.
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'id'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista
     
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
              
    
# 2.- Listar todos los empleados que pertenecen a un área de la empresa.
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            Departamento__short_name = area
             )
        return lista

# 3.- Listar empleados por trabajo. Hecho por mi, como tarea del profe.

class ListByJobEmpleado(ListView):
    template_name = 'persona/list_by_job.html'
    
    def get_queryset(self):
        trabajo = self.kwargs['job']        
        lista = Empleado.objects.filter(
            job = trabajo
             )
        return lista  
    
# 4.- Listar los empleados por palabra clave.
class ListEmpleadosByKword(ListView):
    """" lista empleado por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# 5.- Listar habilidades de un empleado.
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado #obiligatorio este parámetro
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #Crear un proceso para seleccionar el empleado
        context ['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        #lógica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() #metodo interno de la ORM para insertar este dato.
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'Departamento',
        'habilidades',     
        'hoja_vida',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"        
    success_url = reverse_lazy('persona_app:empleados_admin')
    

