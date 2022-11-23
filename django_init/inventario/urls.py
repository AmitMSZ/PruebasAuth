from django.urls import path
from .views import list_product, add_product, edit_product, delete_product, list_warehouse, add_warehouse, edit_warehouse, delete_warehouse, list_type, add_type, edit_type, delete_type

urlpatterns = [
    # CRUD Product
    path('list_product/', list_product, name='list_product'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>', edit_product, name='edit_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
    # CURD Warehouse
    path('list_warehouse/', list_warehouse, name='list_warehouse'),
    path('add_warehouse/', add_warehouse, name='add_warehouse'),
    path('edit_warehouse/<int:pk>', edit_warehouse, name='edit_warehouse'),
    path('delete_warehouse/<int:pk>', delete_warehouse, name='delete_warehouse'),
    # CURD Type
    path('list_type/', list_type, name='list_type'),
    path('add_type/', add_type, name='add_type'),
    path('edit_type/<int:pk>', edit_type, name='edit_type'),
    path('delete_type/<int:pk>', delete_type, name='delete_type'),
]
