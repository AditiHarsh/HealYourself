from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from front.models import patient,doctor
import subprocess
subprocess.call(["python","C:\\Users\\ADITI HARSH\\Desktop\\Project 2020\\getsetdoc_mail\\codenew.py"])


# Create your views here.

def appointform(request):
    if request.method == 'POST':
        name= request.POST['fname']
        phone= request.POST['phone']
        email= request.POST['email']
        age= request.POST['age']
        gender= request.POST['gender']
        doctor= request.POST['doctor']
        
        patient1=patient.objects.create(name=name,phone=phone,email=email,age=age,gender=gender,doctor=doctor)
        #send_mail(
         #  name,phone,'getsetdoc@gmail.com',[email],fail_silently=False
        #)
        patient1.save()
        print('Appointment made !!!')
        messages.info(request,'Thanks for making the appointment !!! Please check your mail for appointment details.')
        return redirect('register')
    else:
        return render(request,'register.html')
    return redirect('/')
    
