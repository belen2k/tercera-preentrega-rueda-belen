
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import UserCreationForm, AuthenticationForm
from .models import  Profesor , Nota , Estudiante
from .forms import ProfesorForm, NotaForm, EstudianteForm
from django.contrib.auth.models import user 
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_profesor')  # Redirige después de guardar
    else:
        form = ProfesorForm()

    return render(request, 'mi_app/form_profesor.html', {'form': form})

def agregar_Nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_Nota')  # Redirige después de guardar
    else:
        form = NotaForm()

    return render(request, 'mi_app/form_Nota.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_estudiante')  # Redirige después de guardar
    else:
        form = EstudianteForm()

    return render(request, 'mi_app/form_estudiante.html', {'form': form})

def inicio(request):
    return render(request,'appbelen/index.html')
def buscar_estudiantes(request):
    """
    Vista para buscar universidades en la base de datos.
    Si el usuario proporciona un nombre, filtra por ese criterio.
    Si no hay búsqueda, muestra todas las universidades.
    """
    # Obtener el parámetro 'q' desde la URL. Si no existe, usar una cadena vacía por defecto.
    query = request.GET.get('q', '')

    # Si hay un término de búsqueda, buscar universidades cuyo nombre coincida parcialmente.
    if query:
        estudiantes = Estudiante.objects.filter(nombre__icontains=query)  # Búsqueda insensible a mayúsculas/minúsculas
    else:
        estudiantes = Estudiante.objects.all()  # Si no hay consulta, mostrar todas las universidades.

    # Renderizar la plantilla y enviar las universidades y la consulta como contexto.
    return render(request, 'appbelen/buscar_estudiante.html', {'estudiantes': estudiantes, 'query': query})


def home(request):
    return render (request, 'home.html')

def signup(request):
   if request.method =='GET':
       return render (request, 'signup.html' {
  'form': UserCreationForm
   })
   else:
       if request.POST['password1'] == request.POST['password2']:
           user = user.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
           user.save()
           login(request, user)
           return redirect('tasks')
           return HttpResponse('Usuario creado satisfactoriamente')


def tasks(request):
    return render(request,'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
   if request.method=='GET':
        return render (request, 'signin.html', {
        'form' : AuthenticationForm
    })
   else:
     user=authenticate(request, username=request.POST['username'], password=request.POST
                     ['password'])
     if user is none:
          return render (request, 'signin.html', {
         'form' : AuthenticationForm
         'error':'username o password es incorrecto '
    })
     else:
        login(request, user)
        return redirect('tasks')



     
       
      


