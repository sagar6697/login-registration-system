from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from django.contrib.auth.views import PasswordResetView
from django.http import HttpResponse
def home(request):

    return render(request,'app1/home.html')


def signup(request):
    if request.method=="POST":
        uname=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pno=request.POST['phoneNo']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(uname,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        subject = 'Welcome to My Website'
        message = 'Thank you for signing up!'
        from_email = 'sagaradlinge6697@gmail.com'  # Aapke email address ko yahan par specify karein
        recipient_list = [email]  # User ka email address

        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, "Your account has been successfully created. An email has been sent to your address.")

        return redirect('signin')


        messages.success(request,"Your account has been suncessfully created!!")
        
        return redirect('signin')


    return render(request,'app1/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            
            return render(request,'app1/index.html')
        else:
            
            return redirect('home')
        
    return render(request, 'app1/signin.html')


def signout(request):

    return render(request,'app1/signout.html')


def index(request):
    return render(request, "app1/index.html")


def signouthome(request):

    return render(request,"app1/signouthome.html")

class CustomPasswordResetView(PasswordResetView):
    template_name = 'app1/password_reset.html'  # The template for the password reset form
    email_template_name = 'app1/password_reset_email.html'  # The email template
