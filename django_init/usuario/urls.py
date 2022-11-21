from django.urls import path
from .views import add_user, soporte, home, list_user, edit_user, delete_user, list_job, add_job, edit_job, delete_job

urlpatterns = [
    path('', home, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('list_user/', list_user, name='list_user'),
    path('edit_user/<int:pk>', edit_user, name='edit_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('add_job/', add_job, name='add_job'),
    path('list_job/', list_job, name='list_job'),
    path('edit_job/<int:pk>', edit_job, name='edit_job'),
    path('delete_job/<int:pk>', delete_job, name='delete_job'),
    path('soporte/', soporte, name='soporte'),
]
