from django.urls import path
from Appbelen import views

urlpatterns = [
  
    path('agregar_profesor/',views.agregar_profesor,name='agregar_profesor' ),
    path('agregar_Nota/',views.agregar_Nota,name='agregar_Nota' ),
    path('agregar_estudiante/',views.agregar_estudiante,name='agregar_estudiante' ), 
    path('inicio/',views.inicio,name='inicio' ),
     path('buscar_estudiantes/',views.buscar_estudiantes,name='buscar_estudiantes' ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/, views.signup', name='signup'),
     path('tasks/, tasks.signup', name='tasks')
]
