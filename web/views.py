from django.shortcuts import redirect,render
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "web/index.html")

def event(request):
    return render(request, "web/eventpage.html")

def eventpost(request):
    return render(request, "web/eventpost.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name1', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('message', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, "web/contact.html")

def service(request):
    return render(request, "web/service.html")

def sign(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['emailid']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your Account has been successfully created.")

        redirect("/signin")

    return render(request, "web/signin.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Check your detail once again!")
            return redirect("/")

    return render(request, "web/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("/")
