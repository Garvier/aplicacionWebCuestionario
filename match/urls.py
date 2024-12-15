from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pregunta/<int:pregunta_id>/', views.mostrar_pregunta, name='mostrar_pregunta'),
    path('curso/<int:curso_id>/', views.mostrar_curso, name='mostrar_curso'),
    path('finalizar/', views.finalizar, name='finalizar'),
]
