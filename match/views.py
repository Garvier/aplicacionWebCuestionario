from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pregunta, Opcion, RespuestaUsuario, Curso, AnoAcademico
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms

# Formulario inicial
class InicioForm(forms.Form):
    email = forms.EmailField()
    curso_actual = forms.ModelChoiceField(queryset=AnoAcademico.objects.all(), empty_label=None)

def inicio(request):
    if request.method == 'POST':
        form = InicioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            curso_actual = form.cleaned_data['curso_actual']

            user, created = User.objects.get_or_create(username=email, defaults={'email': email})
            login(request, user)

            primera_pregunta = curso_actual.pregunta_inicial

            if primera_pregunta:
                return redirect('mostrar_pregunta', pregunta_id=primera_pregunta.id)
            else:
                return redirect('finalizar')
    else:
        form = InicioForm()

    return render(request, 'inicio.html', {'form': form})

def mostrar_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)

    if request.method == 'POST':
        opcion_id = request.POST.get('opcion')
        opcion = get_object_or_404(Opcion, id=opcion_id)

        # Guardar respuesta del usuario
        RespuestaUsuario.objects.create(
            usuario=request.user,
            pregunta=pregunta,
            opcion=opcion
        ).save()


        # Redirigir según la opción seleccionada
        if opcion.siguiente_pregunta:
            return redirect('mostrar_pregunta', pregunta_id=opcion.siguiente_pregunta.id)
        elif opcion.curso_destino:
            return redirect('mostrar_curso', curso_id=opcion.curso_destino.id)
        else:
            return redirect('finalizar')
    else:
        return render(request, 'pregunta.html', {'pregunta': pregunta})

def mostrar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'curso.html', {'curso': curso})

def finalizar(request):
    return render(request, 'finalizar.html')
