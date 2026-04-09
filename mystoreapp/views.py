from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def SignupFnc(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic')
        is_seller = request.POST.get('is_seller')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'This username already exist please try any other name')
        else:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email already exist please try any other email address')
            else:
            
                if is_seller=='on':
                    is_seller=True
                else:
                    is_seller=False
                print('signup time', email, password)
                usercreate = CustomUser.objects.create(username=username, email=email, bio=bio, is_seller=is_seller, profile_pic=profile_pic)
                usercreate.set_password(password)
                usercreate.save()
                messages.success(request, 'Your account is created successfully!')
    return render(request, "sginup.html")

def signinfnc(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        if CustomUser.objects.filter(username=username).exists():
            checkuser = authenticate(request, username=username, password=password)
            if checkuser is not None:
                login(request, checkuser)
                messages.success(request, 'User is logined successfully!')
            else:
                print('wrong password')
                messages.error(request, 'Wrong Password, Please try again.')
        else:
            messages.error(request, "This user dosn't exist")
    return render(request, 'signin.html')

@login_required(login_url='/app/signin')
def index(request):
    return render(request, 'index.html')

def logoutfnc(request):
    logout(request)
    return redirect('/app/signin')

def addproduct(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stk = request.POST.get('stk')
        product_pic = request.FILES.get('product_pic')
        
        
        Product.objects.create(name=name, description=description, price=price, stk_available=stk, picture=product_pic)
    return render(request, 'addproduct.html')

def products(request):
    return render(request, 'products.html')

    
