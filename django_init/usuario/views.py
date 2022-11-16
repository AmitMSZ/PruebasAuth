from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Job, Employee
from .forms import EmployeeForm
# Create your views here.

j = Job()


def soporte(request):
    return render(request, 'registration/soporte.html')

# CRUD Usuarios


@login_required
def home(request):
    return render(request, 'usuario/home.html')


@login_required
def add_user(request):
    data = {
        'form': EmployeeForm()
    }
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request, 'usuario/add_user.html', data)
@login_required
def edit_user(request):
    data = {
        'form': EmployeeForm()
    }
    if request.method == 'PUT':
        form = EmployeeForm(data=request.PUT)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request,'usuario/edit_user.html', data)
@login_required
def list_user(request):
    employee = Employee.objects.all()
    data = {
        'employee': employee
    }
    return render(request, 'usuario/list_user.html', data)
