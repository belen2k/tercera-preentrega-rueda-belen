
# Create your views here.
from django.shortcuts import render, redirect
from .models import Profesor , Nota , Estudiante
from .forms import ProfesorForm, NotaForm, EstudianteForm

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