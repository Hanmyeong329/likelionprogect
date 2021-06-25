
from django.shortcuts import redirect, render,get_object_or_404
from .models import Signup
from django.utils import timezone

# Create your views here.
def home(request):
    signup=Signup.objects.all()
    return render(request,'home.html',{'signup':signup})

def detail(request,id):
    signup=get_object_or_404(Signup,pk = id)
    return render(request,'detail.html',{'signup':signup})

def new(request):
    return render(request,'new.html')
 
def create(request):
    new_introduce=Signup()
    new_introduce.name=request.POST['name']
    new_introduce.age=request.POST['age']
    new_introduce.email=request.POST['email']
    new_introduce.introduce=request.POST['introduce']
    new_introduce.pub_date=timezone.now()
    new_introduce.save()
    return redirect('detail',new_introduce.id)

def edit(request,id):
    edit_signup = Signup.objects.get(id=id)
    return render(request,'edit.html',{'sign':edit_signup})

def update(request,id):
    update_signup=Signup.objects.get(id=id)
    update_signup.name=request.POST['name']
    update_signup.age=request.POST['age']
    update_signup.email=request.POST['email']
    update_signup.introduce=request.POST['introduce']
    update_signup.pub_date=timezone.now()
    update_signup.save()
    return redirect('detail',update_signup.id)

def delete(request,id):
    delete_signup=Signup.objects.get(id=id)
    delete_signup.delete()
    return redirect('home')