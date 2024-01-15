from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        # location = request.POST['location']

        new_emp = Employee(
            first_name= first_name,
            last_name=last_name,
            bonus=bonus,
            salary=salary,
            phone= phone,
            role_id=role,
            dept_id=dept,
            # location=location, 
            hire_date=datetime.now()
            )

        new_emp.save()
        return HttpResponse('Employee Added Successfully')
        
    elif request.method == 'GET': 
        return render(request,'add_emp.html')

    else:
        return HttpResponse('Invalid Request, Employee is not added to the database')


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_tobe_deleted = Employee.objects.get(id = emp_id)
            emp_tobe_deleted.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Employee Not Found')

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps =Employee.objects.all()
        if name:
            emps = emps.filter(first_name__icontains = name) | emps.filter(last_name__icontains = name)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {'emps':emps}
        return render(request,'all_emp.html',context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')
        
    else:
        return HttpResponse('Invalid Request, Employee is not added to the database')

