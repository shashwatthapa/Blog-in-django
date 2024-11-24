from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm,RegisterForm,PostForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                return render(request,'login.html',{'form':form,'error':'Invalid username or password'})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form,'error':'Invalid credentials'})
    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

# @login_required
def dashboard(request):
    mem = Post.objects.all().order_by('-id')
    return render(request, 'dashboard.html', {'mem': mem})

def logout_views(request):
    logout(request)
    return redirect('login')
    
@login_required
def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm()
        return render(request,'add.html',{'form':form})

@login_required
def delete(request,id):
    mem = get_object_or_404(Post,id=id)
    mem.delete()
    return redirect('dashboard')

@login_required
def update(request,id):
    mem = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=mem)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=mem)
        return render(request,'update.html',{'form':form,'mem':mem})