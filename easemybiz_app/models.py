from django.db import models

# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.gender

class Employee(models.Model):
    emp_id = models.CharField(max_length=12, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=10)
    email = models.EmailField()
    salary = models.BigIntegerField()
    position = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    due_datetime = models.DateTimeField()
    description = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    appointment_datetime = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.customer_name} on {self.appointment_datetime}"
