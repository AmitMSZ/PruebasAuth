from django.urls import path
from usuario import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('add_user', views.add_user, name='add_user'),
    path('soporte', views.soporte, name='soporte'),
]
