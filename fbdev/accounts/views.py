from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from accounts.models import MyModel
# Create your views here.


#@login_required(login_url='index')
def home(request):
    return render(request, 'index.html')
 
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.save()

        messages.success(request, "You're successfully enrolled.")
        return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)


        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Wrong Credentials")

            return redirect('home')
    return render(request, 'signin.html')
    
def dashboard(request):
    user_data = MyModel.objects.filter(username=request.user.username).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')

        dir = MyModel(username = username, fname = fname, lname = lname, email = email, address = address, city = city, country = country)

        dir.save()
        #return redirect('dashboard')
    
    context = {}

    if user_data:
        context['user_data'] = user_data
    else:
        context['show_form'] = True

    return render(request, 'dashboard.html', context)

def signout(request):
   pass
