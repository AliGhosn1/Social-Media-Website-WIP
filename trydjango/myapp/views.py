from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from django.urls import reverse
from django.template import loader
from .models import jadenSite, SiteUsers , Image
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm;
from .forms import UserCreation , ImageForm
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
    thingsinDatabase = {
        'men': men,
        'users': Users
    }
    return HttpResponse(template.render(thingsinDatabase, request))


def alisite(request):
    template = loader.get_template('tester.html')
    return HttpResponse(template.render())


def createWorkers(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({}, request))


def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['email']
    data3 = request.POST['password']
    newUser = SiteUsers(name=data1, email=data2, password=data3)
    newUser.save()
    return HttpResponseRedirect(reverse('login'))


def loginPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # user = authenticateUser(request)
        user = authenticate(request, username=name, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('userSite/')
        else:
            messages.success(request, 'incorrect username or password')
    context = {}
    return render(request, 'login.html', context)


# sdasdasdasd


def register(request):
    form = UserCreation
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'account was succesfully made for ' + username)
            newUser = SiteUsers.objects.create(name=username)
            newUser.save()
            return redirect('login')
    context = {'form': form}
    print("dsadasdasd")
    return render(request, 'register3.html', context)  # render must take a dict so put form in dictionarysasa

'''
def upload(request):
    if request.method == 'POST':
        user= request.user.username
        image = request.FILES.get("image")
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user,image=image , caption=caption)
        new_post.save();
        posts = Post.objects.all()
        return render(request, 'post1.html', {'posts':posts,'user': user,'image':image , 'caption':caption})
    else:
        return render(request ,'post1.html',{'image':request.FILES.get("image")})
'''


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = request.user.username
            posts = Image.objects.all()
            image = request.FILES.get("image")
            img_obj = form.instance
            return render(request, 'post1.html', {'form': form, 'img_obj': img_obj , 'posts':posts , 'user':user , 'image':image})
    else:
        form = ImageForm()
    return render(request, 'post1.html', {'form': form})

def userSite(request):
    if request.user.username == "":
        return redirect('login')
    else:
        context = {
            'NAME':request.user.username,
            'PFP':SiteUsers.objects.get(name=request.user.username).picture
        }
        return render(request,'userPage.html', context)
