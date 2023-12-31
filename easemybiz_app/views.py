from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Task, Expense, Appointment
from django.utils.timezone import make_aware
from datetime import datetime

# Create your views here.

def home(request):
    inprogress = Task.objects.filter(completed=False)
    expenses = Expense.objects.all()
    appointments = Appointment.objects.all()
    return render(request, "dashboard.html", context={"tasks": inprogress, "expenses": expenses, "appointments": appointments})

def manage_employees(request):
    employees = Employee.objects.all()
    return render(request, "manage_emp.html", context={'employees': employees})

def add_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        gender = int(request.POST['gender'])
        ph_no = request.POST['ph_no']
        email = request.POST['email']
        position = request.POST['position']
        salary = int(request.POST['salary'])
        employee = Employee(name=name, emp_id=emp_id, gender_id=gender,
                            ph_no=ph_no, email=email, position=position, salary=salary)
        employee.save()
        return redirect(manage_employees)
    else:
        return render(request, 'add_emp.html')


def delete_emp(request, id=0):
    if request.method == 'POST':
        employees = list(request.POST)
        if employees[1] == 'all':
            Employee.objects.all().delete()
        else:
            for i in range(1,len(employees)):
                Employee.objects.get(emp_id=employees[i]).delete()
    return redirect(manage_employees)


def task_manager(request):
    inprogress = Task.objects.filter(completed=False)
    completed = Task.objects.filter(completed=True)
    return render(request, "task_manager.html", context={"inprogress": inprogress, "completed": completed})

def task_complete(request, id=0):
    task = Task.objects.get(pk=id)
    task.completed = True
    task.save()
    return redirect(task_manager)

def task_delete(request, id=0):
    Task.objects.get(pk=id).delete()
    return redirect(task_manager)

def task_add(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        due_datetime = request.POST['due_datetime']
        assigned_to = int(request.POST['assigned'])
        task = Task(title=title, description=description, due_datetime= due_datetime, assigned_to_id = assigned_to)
        task.save()
        return redirect(task_manager)
    else:
        employees = Employee.objects.all()
        return render(request, "add_task.html", context={'employees': employees})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        category = request.POST.get('category')
        
        Expense.objects.create(
            description=description,
            amount=amount,
            date=date,
            category=category
        )
        return redirect('expense_list')
        
    return render(request, 'add_expense.html')

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        category = request.POST.get('category')
        
        expense.description = description
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.save()
        
        return redirect('expense_list')
    
    return render(request, 'edit_expense.html', {'expense': expense})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    
    return render(request, 'delete_expense.html', {'expense': expense})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

def create_appointment(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        service_name = request.POST['service_name']
        appointment_datetime = make_aware(datetime.strptime(request.POST['appointment_datetime'], '%Y-%m-%dT%H:%M'))
        notes = request.POST.get('notes', '')
        
        Appointment.objects.create(
            customer_name=customer_name,
            service_name=service_name,
            appointment_datetime=appointment_datetime,
            notes=notes
        )
        return redirect('appointment_list')
    return render(request, 'appointment_form.html')

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.customer_name = request.POST['customer_name']
        appointment.service_name = request.POST['service_name']
        appointment.appointment_datetime = make_aware(datetime.strptime(request.POST['appointment_datetime'], '%Y-%m-%dT%H:%M'))
        appointment.notes = request.POST.get('notes', '')
        appointment.save()
        return redirect('appointment_detail', appointment_id=appointment_id)
    return render(request, 'appointment_form.html', {'appointment': appointment})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_confirm_delete.html', {'appointment': appointment})
