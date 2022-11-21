from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import jadenSite , SiteUsers
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreation

# Create your views here.

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
    Users = SiteUsers.objects.all().values()
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        #change authenticate method it is using the default admin and not the SiteUser lol
        user = authenticate(request,username=name, password=password)
        print(name,password)
        if user is not None:
            login(request,user)
            return redirect('jadenSite/')

    context = {}
    return render(request ,'login.html',context)
#sdasdasdasd


def register(request):
    form = UserCreation
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request,'register.html',context)#render must take a dict so put form in dictionary


