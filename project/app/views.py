from django.shortcuts import render,redirect
from app.models import Employees

def Index(request):
    emp=Employees.objects.all()

    context ={
        'emp':emp,
    }


    return render(request,'index.html',context)

# Create your views here.
def Add(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp=Employees(
            name =name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return render(request,'index.html')

def Edit(request):
    emp=Employees.objects.all()

    context ={
        'emp':emp,
    }
    return redirect(request,'index.html',context)

def Update(request,id):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp=Employees(
            id=id,
            name =name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return redirect(request,'index.html')
