import csv
from datetime import datetime, date

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contactinfo,Signupinfo
def Home(request):
     return render(request,'home.html')

def Menu(request):
    return render(request,'menu.html')

def About(request):
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Customers(request):
   #page = request.GET['page']
   #print(page)
    #with connection.cursor() as cursor:
        #cursor.execute("SELECT * FROM employee")
        #list = cursor.fetchall()
   list = Contactinfo.objects.all()
   paginator = Paginator(list, 2)  # Show 2 contacts per page.
   page_number = request.GET.get('page')
   list = paginator.get_page(page_number)
   return render(request, 'customers.html',{'list':list})

def Contact(request):
    if request.method == "POST":
        message=request.POST['message'];
        name = request.POST['name'];
        email = request.POST['email'];
        subject = request.POST['subject'];
        img=request.FILES['image']
        contact=Contactinfo(message=message,name=name,email=email,subject=subject,file=request.FILES['image'])
        contact.save()
        messages.success(request,"Requested successfully sent")
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
def Export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Email Address','Message','Subject'])
    users = Contactinfo.objects.all().values_list('name','email','message','subject')
    for user in users:
        writer.writerow(user)
    return response
def Search(request):
    if(request.POST['smessage']):
        list = Contactinfo.objects.filter(message__contains=request.POST['smessage'])
    else:
        list = Contactinfo.objects.all()
    return render(request, 'customers.html', {'list': list})
def Signup(request):
    if request.method == "POST":
        name=request.POST['name'];
        email = request.POST['email'];
        psw = request.POST['psw'];
        todaydate=date.today();
        cdatetime = datetime.now()
        signup=Signupinfo(name=name,email=email,password=psw,date=todaydate,datetime=cdatetime)
        signup.save()
        messages.success(request,"Registered Successfully")
        return render(request,'home.html')
    else:
        return render(request, 'home.html')
def Login(request):
    if(request.POST):
        email = request.POST['email'];
        password = request.POST['password'];
        try:
            respon=Signupinfo.objects.get(email__exact=email,password=password)
            request.session['loggedid']=respon.id;
            messages.success(request, "Login Successfully")
            return render(request,'home.html')
        except Signupinfo.DoesNotExist:
            messages.success(request, "Login Failed Try Again")
            return render(request,'home.html')
    else:
        return render(request, 'home.html')
def Logout(request):
    del request.session['loggedid'];
    messages.success(request, "Log Out Successfully")
    return render(request,'home.html')