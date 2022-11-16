from django.urls import path
from .views import add_user, soporte, home, list_user, edit_user, delete_user

urlpatterns = [
    path('', home, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('list_user/', list_user, name='list_user'),
    path('edit_user/<int:pk>', edit_user, name='edit_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('soporte/', soporte, name='soporte'),
]
