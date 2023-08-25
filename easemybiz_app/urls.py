from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('employees/',views.manage_employees, name="manage_employees"),
    path("add_emp/", views.add_emp, name="add_emp"),
    path('delete_emp/',views.delete_emp, name="delete_emp"),
    path("task_manager/", views.task_manager, name="task_manager"),
    path("task_complete/<int:id>", views.task_complete, name="task_complete"),
    path("task_delete/<int:id>", views.task_delete, name="task_delete"),
    path("task_add/", views.task_add, name="task_add"),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add_expense/', views.add_expense, name='add_expense'),
    path('expenses/edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]