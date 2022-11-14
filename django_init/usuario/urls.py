from django.urls import path
from .views import add_user, soporte, home, list_user

urlpatterns = [
    path('', home, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('list_user/', list_user, name='list_user'),
    path('soporte/', soporte, name='soporte'),
]
