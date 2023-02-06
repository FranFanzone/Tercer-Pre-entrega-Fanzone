from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *

def inicio(request):

    return render(request,'App1/inicio.html')

def verProfesorFormulario(request):

    if request.method == 'POST':

        formularioProfesor = ProfesorFormulario(request.POST)

        if formularioProfesor.is_valid():

            info = formularioProfesor.cleaned_data

            profe = Profesor(nombre = info['nombre'],
                             apellido = info['apellido'],
                             materia = info['materia'],
                             fecha_nacimiento = info['fecha_nacimiento'],
                             email = info['email']
                             )
            profe.save()
            return render(request, 'App1/inicio.html')
    else:
        
        formularioProfesor = ProfesorFormulario()
    
    return render(request, 'App1/verProfesor.html', {'formProfe':formularioProfesor})

def verAlumnoFormulario(request):

    if request.method == 'POST':

        formularioAlumno = AlumnoFormulario(request.POST)

        if formularioAlumno.is_valid():

            info = formularioAlumno.cleaned_data

            alumn = Alumno(nombre = info['nombre'],
                          apellido = info['apellido'],
                          materia = info['materia'],
                          fecha_nacimiento = info['fecha_nacimiento'],
                          email = info['email'])
            alumn.save()
            return render(request, 'App1/inicio.html')
    else: 
        formularioAlumno = AlumnoFormulario()

    return render(request, 'App1/verAlumno.html', {'formAlumn':formularioAlumno})

def verCarreraFormulario(request):

    if request.method == 'POST':

        formularioCarrera = CarreraFormulario(request.POST)

        if formularioCarrera.is_valid():

            info = formularioCarrera.cleaned_data

            carrer = Carrera(nombre = info['nombre'],
                             materias = info['materias'])
            carrer.save()
            return render(request, 'App1/inicio.html')
    else:
        formularioCarrera = CarreraFormulario()
    
    return render(request, 'App1/verCarrera.html', {'formCarrera':formularioCarrera})

def verEntregableFormulario(request):

    if request.method == 'POST':

        formularioEntregable = EntregableFormulario(request.POST)

        if formularioEntregable.is_valid():

           info = formularioEntregable.cleaned_data

           entregabl = Entregable(materia = info['materia'],
                                   entregado = info['entregado'])
           entregabl.save()
           return render(request, 'App1/inicio.html')
    else:
        formularioEntregable = EntregableFormulario()
    
    return render(request, 'App1/verEntregable.html', {'formEntregable':formularioEntregable})

def busquedaProfesor(request):

    return render(request, 'App1/inicio.html')

def resultadoBProfesor(request):

    if request.GET['nombre']:
       
         nombre = request.GET['nombre']
         profesores = Profesor.objects.filter(nombre__icontains=nombre)

         return render(request, 'App1/verProfesor.html', {'profesores':profesores, 'nombre':nombre})
    else:        
        respuesta = 'No buscaste nada'

        return render(request, 'App1/verProfesor.html', {'respuesta':respuesta})

    return HttpResponse(respuesta)

def busquedaAlumno(request):

    return render(request, 'App1/inicio.html')

def resultadoBAlumno(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)

        return render(request, 'App1/verAlumno.html', {'alumnos':alumnos, 'nombre':nombre})
    else:
        respuesta = 'No buscaste nada'
        return render(request, 'App1/verAlumno.html', {'respuesta':respuesta})
    
    return HttpResponse(respuesta)

def busquedaCarrera(request):

    return render(request, 'App1/inicio.html')

def resultadoBCarrera(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        carreras = Carrera.objects.filter(nombre__icontains=nombre)

        return render(request, 'App1/verCarrera.html', {'carreras':carreras, 'nombre':nombre})
    else:
        respuesta = 'No buscaste nada'
        return render(request, 'App1/verCarrera.html', {'respuesta':respuesta})
    
    return HttpResponse(respuesta)

def busquedaEntregable(request):

    return render(request, 'App1/inicio.html')

def resultadoBEntregable(request):

    if request.GET['materia']:

        materia = request.GET['materia']
        entregables = Entregable.objects.filter(materia__icontains=materia)

        return render(request, 'App1/verEntregable.html', {'entregables':entregables, 'materia':materia})
    else:
        respuesta = 'No buscaste nada'
        return render(request, 'App1/verEntregable.html', {'respuesta':respuesta})
    
    return HttpResponse(respuesta)