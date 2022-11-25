from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Warehouse, Type, Product
from .forms import WarehouseForm, TypeForm, ProductForm

# Create your views here.

# CRUD Warehouse/Bodega


@login_required
def add_warehouse(request):
    data = {
        'form': WarehouseForm()
    }
    if request.method == 'POST':
        form = WarehouseForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request, 'inventario/add_product.html', data)


@login_required
def edit_warehouse(request, pk):
    warehouse = Warehouse.objects.get(warehouse_id=pk)
    form = WarehouseForm(instance=warehouse)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
    elif request.method == 'PUT':
        form = WarehouseForm(request.PUT, instance=warehouse)
    data = {'form': form}
    return render(request, 'inventario/edit_product.html', data)


@login_required
def delete_warehouse(request, pk):
    warehouse = Warehouse.objects.get(warehouse_id=pk)
    if request.method == "POST":
        warehouse.delete()
    data = {'product': warehouse}
    return render(request, 'inventario/delete_product.html', data)


@login_required
def list_warehouse(request):
    search = request.GET.get("search")
    warehouse = Warehouse.objects.all()

    if search:
        warehouse = Warehouse.objects.filter (
            Q(warehouse_name__icontains = search)
        )

    data = {
        'warehouse': warehouse
    }
    return render(request, 'inventario/list_warehouse.html', data)


# CRUD Type/Tipo

@login_required
def add_type(request):
    data = {
        'form': TypeForm()
    }
    if request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request, 'inventario/add_product.html', data)


@login_required
def edit_type(request, pk):
    type = Type.objects.get(type_id=pk)
    form = TypeForm(instance=type)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
    elif request.method == 'PUT':
        form = TypeForm(request.PUT, instance=type)
    data = {'form': form}
    return render(request, 'inventario/edit_product.html', data)


@login_required
def delete_type(request, pk):
    type = Type.objects.get(type_id=pk)
    if request.method == "POST":
        type.delete()
    data = {'product': type}
    return render(request, 'inventario/delete_product.html', data)


@login_required
def list_type(request):

    search = request.GET.get("search")
    type = Type.objects.all()

    if search:
        type = Type.objects.filter(
            Q(type_name__icontains = search) 
        )

    data = {
        'type': type
    }


    return render(request, 'inventario/list_type.html', data)


# CRUD Products/Productos

@login_required
def add_product(request):
    data = {
        'form': ProductForm()
    }
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            data["form"] = form
    return render(request, 'inventario/add_product.html', data)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(product_id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
    elif request.method == 'PUT':
        form = ProductForm(request.PUT, instance=product)
    data = {'form': form}
    return render(request, 'inventario/edit_product.html', data)


@login_required
def delete_product(request, pk):
    product = Product.objects.get(product_id=pk)
    if request.method == "POST":
        product.delete()
    data = {'product': product}
    return render(request, 'inventario/delete_product.html', data)


@login_required
def list_product(request):

    search = request.GET.get("search")
    product = Product.objects.all()
    # check el filtro sobre una llave foranea
    if search:
        product = Product.objects.filter (
            Q(product_name__icontains = search) |
            Q(product_description__icontains = search) 
        ).distinct()

    data = {
        'product': product
    }
    return render(request, 'inventario/list_product.html', data)
