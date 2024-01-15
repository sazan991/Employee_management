from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('all_emp',views.all_emp,name='all_emp.html'),
    path('add_emp',views.add_emp,name='add_emp.html'),
    path('remove_emp',views.remove_emp,name='remove_emp.html'),
    path('remove_emp/<int:emp_id>',views.remove_emp,name='remove_emp.html'),
    path('filter_emp',views.filter_emp,name='filter_emp.html'),
]