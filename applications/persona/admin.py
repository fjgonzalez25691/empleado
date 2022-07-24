from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'Departamento',
        'job',
        'full_name',
    )    
    #
    def full_name(self, obj):
        return  obj.last_name + ', ' + obj.first_name 

    search_fields = ('first_name',)
    list_filter = ('Departamento','job','habilidades',  )
    #
    filter_horizontal = ('habilidades',) 
    
    
admin.site.register(Empleado, EmpleadoAdmin)