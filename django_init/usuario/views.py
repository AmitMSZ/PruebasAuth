from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def soporte(request):
    return render(request, 'registration/soporte.html')


@login_required
def inicio(request):
    usuario = User.objects.all()
    context = {
        'usuario': usuario
    }
    return render(request, 'usuario/base.html', context)


@login_required
def add_user(request):
    return render(request, 'usuario/add_user.html')
