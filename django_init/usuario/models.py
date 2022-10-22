from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.CharField('Cargo', max_length=30, unique=True)

    class Meta:
        db_table = 'job'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.job


class UserManager(BaseUserManager):
    def _create_user(self, username,job,email, name, last_name, password, is_staff, is_superuser,**extra_fields):
        user = self.model(
            username = username,
            job = job,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self,username,job,email,name,last_name,password= None,**extra_fields):
        return self._create_user(username,job,email,name,last_name,password,False,False,**extra_fields)
    
    def create_superuser(self,username,job,email,name,last_name,password= None,**extra_fields):
        return self._create_user(username,job,email,name,last_name,password,True,True,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job,null =True,on_delete=models.CASCADE)

    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=30)
    name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellido', max_length=70)
    email = models.EmailField('Correo Electronico', max_length=50, unique=True)
    #date_create = models.DateField('Fecha de Creacion', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['job','email', 'name', 'last_name']

    class Meta:
        db_table = 'user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name
    
