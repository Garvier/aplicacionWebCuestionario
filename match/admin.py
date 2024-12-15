from django.contrib import admin
from .models import Pregunta, Opcion, Curso, AnoAcademico, ImagenFondo

class OpcionInline(admin.TabularInline):
    model = Opcion
    fk_name = 'pregunta_origen'
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]
    list_display = ('label', 'texto')
    search_fields = ('label', 'texto')

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Curso)
admin.site.register(AnoAcademico)
admin.site.register(ImagenFondo)