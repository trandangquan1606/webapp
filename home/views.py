from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.form import RegistrationForm
from django.contrib import messages
from blog.models import Post

# Create your views here.
def index(request): 
    return render(request,'page/base1.html')
def crregister(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form =  RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    Data  = {'form':form}
    
def home(request): 
    return render(request,'page/home.html')
def contact(request):
    return render(request, 'page/contact.html')
def error(request, exception):
    return render(request, 'error.html', status=404)
def error_500(request):
    return render(request, 'error_500.html', status=500)
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'page/register.html', {'form': form})
def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            print('login')
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect("/home")
        else:
            print('inlogin')
            messages.error(request, "Invalid Credentials")
        return render(request, 'page/login.html')   
    return render(request, "page/login.html")
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(pass1 != pass2):

            messages.error(request,'confirm password must match password!')
            redirect('/')
        try:
    
            # check user existed
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('/')
            User.objects.create_user(username=username,password=pass1,is_active=True,is_staff=True)
            user = User.objects.all()
        
        except: User.DoesNotExist
    else:
        HttpResponseRedirect('/')
    return render(request, "page/login.html")