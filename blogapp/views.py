from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from blogapp import models
from .models import Post,Comment,Author
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm,CommentForm,AuthorForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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


@login_required
def home(request):
    return render(request, 'base.html') 


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all() 
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
                return redirect('post_detail', pk=post.pk) 
        else:
            return redirect('login')
    else:
        form = CommentForm() 
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})



def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete comments on this post.")

    if request.method == "POST":
        comment.delete()
        return redirect('mypost_detail', pk=post.pk)

    return redirect('mypost_detail', pk=post.pk)


def author_list(request):
    authors=Author.objects.all()
    return render(request,'author_list.html',{'authors':authors})


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            return redirect('author_detail', pk=new_author.pk)
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})



def author_detail(request,pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=author.pk) 
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})


def author_delete(request,pk):
    author=get_object_or_404(Author,pk=pk)
    if request.method=='POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_delete.html', {'author': author})
