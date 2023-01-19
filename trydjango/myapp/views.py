from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from django.urls import reverse
from django.template import loader
from .models import jadenSite, SiteUsers , Image , Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User , auth
from django.contrib.auth.forms import UserCreationForm
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
    Users = SiteUsers.objects.all().values().values()

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
            return redirect('upload/')
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
            user = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            # if User.objects.filter(email=email).exists():
            #     print("zzzzzzzzz")
            #     messages.info(request,'email already in use')
            #     return redirect('register')
            # elif User.objects.filter(user=user).exists():
            #     print("bbbbbbbbb")
            #     messages.info(request,'username already in use')
            #     return redirect('register')
            # else:
            print("dsadasdasdasddsa")
            user_model = User.objects.get(username=user)
            new_profile = Profile.objects.create(user=user_model,userId =user_model.id)
            new_profile.save()
            #return redirect('login')
            #messages.success(request, 'account was succesfully made for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register3.html', context)  # render must take a dict so put form in dictionarysasa



def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.username
            image = request.FILES.get("image")
            title = request.POST.get('title')
            new_post = Image.objects.create(user=user, image=image, title=title, userWhoPosted = User.objects.get(username = user))
            new_post.save()
            posts = Image.objects.all()
            pfp = Profile.objects.all().values()
            print(pfp)
            render(request, 'post1.html', {'form': form , 'posts':posts , 'user':user , 'image':image,'pfp':pfp})
            return redirect('upload')
    else:
        form = ImageForm()
        posts = Image.objects.all()
        return render(request, 'post1.html', {'form': form , 'posts':posts})


def userSite(request):
    if request.user.username == "":
        return redirect('login')
    else:
        context = {
            'NAME':request.user.username,
            'PFP':SiteUsers.objects.get(name=request.user.username).picture
        }
        return render(request,'userPage.html', context)

def profile(request ,pk):
    userReference = User.objects.get(username=pk)
    userProfile = Profile.objects.get(user=userReference)
    userPosts=Image.objects.filter(user=pk)
    numberOfPosts=len(userPosts)
    context ={
        'userPosts':userPosts,
        'numberOfPosts':numberOfPosts,
        'userProfile':userProfile,
    }
    return render(request, 'profile.html',context)