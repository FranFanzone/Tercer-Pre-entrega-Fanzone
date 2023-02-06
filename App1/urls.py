from django.urls import path
from App1.views import *

urlpatterns = [
    path('', inicio, name='incio'),
    path('verProfesor/', verProfesorFormulario, name='verProfesor'),
    path('verAlumno/', verAlumnoFormulario, name='verAlumno'),
    path('verCarrera/', verCarreraFormulario, name='verCarrera'),
    path('verEntregable/', verEntregableFormulario, name='verEntregable'),
    path('busquedaProfesor/', busquedaProfesor, name='busquedaProfesor'),
    path('resultadoProfesor/', resultadoBProfesor, name='resultadoBProfesor'),
    path('busquedaAlumno/', busquedaAlumno, name='busquedaAlumno'),
    path('resultadoAlumno/', resultadoBAlumno, name='resultadoBAlumno'),
    path('busquedaCarrera/', busquedaCarrera, name='busquedaCarrera'),
    path('resultadoCarrera/', resultadoBCarrera, name='resultadoBCarrera'),
    path('busquedaEntregable/', busquedaEntregable, name='busquedaEntregable'),
    path('resultadoEntregable/', resultadoBEntregable, name='resultadoBEntregable'),




]