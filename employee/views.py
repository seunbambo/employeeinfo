from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee  
# Create your views here.

def index(request):  
    #employees = Employee.objects.all()  
    return render(request,"index.html")  

def create(request):
    print(request.POST)
    form = EmployeeForm(request.POST or None)
    
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/list')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'add.html',{'form':form})  
def lists(request):  
    employees = Employee.objects.all()  
    return render(request,"list.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/list")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/list") 