from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Employee, User
from .forms import EmployeeForm, JobForm

# Create your views here.

j = Job()


def soporte(request):
    return render(request, 'registration/soporte.html')


# def login(request):
#   if request.user.is_authenticated():
#        return redirect("/")


# CRUD Usuarios
@login_required
def home(request):
    #    if request.user.employee.job == '':
    #        print(request.user.employee.job)
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
def edit_user(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/list_user/')
    elif request.method == 'PUT':
        form = EmployeeForm(request.PUT, instance=employee)
    data = {'form': form}
    return render(request, 'usuario/edit_user.html', data)


@login_required
def delete_user(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('/list_user/')
    data = {'employee': employee}
    return render(request, 'usuario/delete_user.html', data)


@login_required
def list_user(request):

    search = request.GET.get("search")
    employee = Employee.objects.all()

    # lo que hace Q es buscar por cada atributo coincidencias con lo escrito en el buscador
    
    if search:
        employee = Employee.objects.filter (
            Q(name__icontains = search) |
            Q(last_name__icontains = search) |
            Q(username__icontains = search) |
            Q(email__icontains = search) 
        ).distinct()

    data = {
        'employee': employee
    }
    return render(request, 'usuario/list_user.html', data)


@login_required
def add_job(request):
    data = {
        'form': JobForm()
    }
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request, 'usuario/add_job.html', data)


@login_required
def edit_job(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
    elif request.method == 'PUT':
        form = JobForm(request.PUT, instance=job)
    data = {'form': form}
    return render(request, 'usuario/edit_job.html', data)


@login_required
def delete_job(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        job.delete()
    data = {'job': job}
    return render(request, 'usuario/delete_job.html', data)


@login_required
def list_job(request):

    search = request.GET.get("search")
    job = Job.objects.all()
    

    if search:
        job = Job.objects.filter (
            Q(job__icontains = search) 
        )

    data = {
        'job': job
    }
    return render(request, 'usuario/list_job.html', data)
