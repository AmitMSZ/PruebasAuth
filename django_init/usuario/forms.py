from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Job


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ["username", "name",
                  "last_name", "email", "is_active", "job"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
