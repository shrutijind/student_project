from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, LeaveRequest

admin.site.register(Student)
admin.site.register(LeaveRequest)