from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from blogapp import models
from .models import Post
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'signup.html')


def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/base')
        else:
            return redirect('/loginn')
    return render(request, 'loginn.html')




def base(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'base.html', {'posts': posts})



def myPost(request):
    posts = Post.objects.filter(author=request.user) 
    return render(request, 'mypost.html', {'posts': posts})



def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('my-post')
    
    return render(request, 'newpost.html')



def signout(request):
    logout(request)
    return redirect('/loginn')


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('mypost_detail',pk=post.pk) 
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form , 'post': post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('my-post')  
    return render(request, 'delete.html', {'post': post})

def my_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mypost_detail.html', {'post': post})

def home(request):
    return render(request, 'base.html') 

