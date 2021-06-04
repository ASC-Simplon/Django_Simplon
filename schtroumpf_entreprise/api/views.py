from django.shortcuts import render, redirect
from .models import Employe
from .forms import EmployeForm
from .models import Department
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {})

def form_employe(request):
    if (request.method == "POST"):
        form = EmployeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('./listEmployees')
            except:
                print('Error in saving the form')
                pass
        else:
            print('The form is not valid.')
    else:
        form = EmployeForm()

    context={'form': form}
    return render(request, 'home/form.html', context)

def listEmployes(request):
    employees = Employe.objects.all()
    context={'employees': employees}
    return render(request, "home/listEmployes.html", context)

def updateEmploye(request, id):
    employee = Employe.objects.get(id=id)
    if (request.method == "POST"):
        form = EmployeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("list_e")
    context = {'employee': employee}
    return render(request, 'home/updateEmploye.html', context)

def deleteEmploye(request, id):
    employee = Employe.objects.get(id=id)
    employee.delete()
    return redirect("list_e")


def searchEmploye(request):
    context={}
    clicked=False
    if(request.method=="POST"):
        clicked = True
        id = request.POST['id']
        try:
            employee = Employe.objects.get(id=id)
            context = {'employee': employee, 'clicked':clicked}
            return render(request, 'home/showEmploye.html', context)
        except ObjectDoesNotExist:
            print("Employee does not exist")
            context ={'clicked':clicked}
            return render(request, 'home/showEmploye.html',context)
    else:
        return render(request, 'home/showEmploye.html')