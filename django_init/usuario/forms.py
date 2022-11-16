from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ["username", "name",
                  "last_name", "email", "is_active", "job"]
