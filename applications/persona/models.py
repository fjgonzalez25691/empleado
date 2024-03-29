from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)   
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
        
    
# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla Empleados"""
    JOB_CHOICES = (
        ('0', 'CONTABLE'),
        ('1', 'ADMINISTRATIVO'),
        ('2', 'GERENTE'),
        ('3', 'GESTOR'),
        ('4',  'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField(
        'Nombre completo',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'Departamento']
        unique_together = ('first_name', 'Departamento')      
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name