from django.contrib import admin
from .models import Gender, Employee, Task, Appointment
# Register your models here.

admin.site.register(Gender)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Appointment)
