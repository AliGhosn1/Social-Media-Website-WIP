from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import jadenSite, SiteUsers
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm;
from .forms import UserCreation
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.
def authenticateUser(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    print(name, password)
    try:
        user = SiteUsers.objects.get(name=name)
    except SiteUsers.DoesNotExist:
        return None
    if user is not None and user.password == password:
        return user
    else:
        return None

def jadenWebsite(request):
    men = jadenSite.objects.all().values()
    Users = SiteUsers.objects.all().values()

    template = loader.get_template('index.html')
    thingsinDatabase ={
        'men':men,
        'users':Users
    }
    return HttpResponse(template.render(thingsinDatabase,request))

def alisite(request):
    template = loader.get_template('tester.html')
    return HttpResponse(template.render())

def createWorkers(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({},request))

def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['email']
    data3 = request.POST['password']
    newUser = SiteUsers(name= data1,email = data2,password = data3)
    newUser.save()
    return HttpResponseRedirect(reverse('login'))


def loginPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        #user = authenticateUser(request)
        user = authenticate(request,username=name,password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('userSite/')
        else:
            messages.success(request, 'incorrect username or password')
    context = {}
    return render(request ,'login.html',context)
#sdasdasdasd


def register(request):
    form = UserCreation
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'account was succesfully made for '+ username)
            newUser = SiteUsers.objects.create(name=username, picture="https://i.pinimg.com/736x/dd/f0/11/ddf0110aa19f445687b737679eec9cb2.jpg")
            newUser.save()
            return redirect('login')
    context = {'form': form}
    return render(request,'register3.html',context)#render must take a dict so put form in dictionary

def userSite(request):
    if request.user.username == "":
        return redirect('login')
    else:
        context = {
            'NAME':request.user.username,
            'PFP':SiteUsers.objects.get(name=request.user.username).picture
        }
        return render(request,'userPage.html', context)