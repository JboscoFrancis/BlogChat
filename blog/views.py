from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import PostForm, UserRegistration, ReplyForm, UpdateProfileForm, UpdatePicture
from . filter import PostFilter
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . decorator import unauthenticated_user, allowed_users

# Create your views here.

def home(request):
    post = Post.objects.all().order_by('-date_created')
    reply = Reply.objects.all().order_by('-reply_date')

    # filter
    postFilter = PostFilter(request.GET, queryset = post)
    post = postFilter.qs

    #paginator for 8 post each page
    paginator = Paginator(post, 8)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    #if user is login, the he/she will see total post he posted
    if request.user.is_authenticated:
        num_post = Post.objects.filter(post_user=request.user).count()
        context = {'post': post, 'reply': reply, 'postFilter':postFilter, 'num_post':num_post}
    else:
    
    #render data to the html page
        context = {'post': post, 'reply': reply, 'postFilter':postFilter,}
    return render(request, 'blog/home.html', context)


@unauthenticated_user       #this check if user is authenticated/logged in, then no need to see register page
def register(request):
    form = UserRegistration()   #create a form
    if request.method == 'POST':
        form = UserRegistration(request.POST)   #if request == POST, then take the data from the form
        if form.is_valid():
            form.save() #save form data
            return redirect('login')
        else:
            messages.info(request, f'something wrong with a form')
    context = {'form': form}
    return render(request, 'blog/register.html', context)

@unauthenticated_user       #this check if user is authenticated/logged in, then no need to see register page
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, f'Sorry username or password is incorrect, Note: username/password is case sensitive')
    return render(request, 'blog/login.html')


#logout user
def userlogout(request):
    logout(request)
    return redirect('home')



@login_required(login_url = 'login')    #this decorator restrict user from creating post before login
def createpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if request.user.is_authenticated:
            form.instance.post_user = request.user  #this take logged in user as the post user
            if form.is_valid():
                form.save()
                messages.info(request, f'Your Post added successfully')
                return redirect('home')
            else:
                messages.info(request, f'Please something wrong with a Post')
        else:
            messages.info(request, f'Please Login required before you add Post')
    context = {'form': form}
    return render(request, 'blog/create.html', context)

#this let you to see a full post of a specific post id
def postdetail(request,pk):
    form = ReplyForm()
    post = Post.objects.get(id=pk)
    reply = post.reply_set.all().order_by('-reply_date')
    total_reply = reply.count()

    paginator = Paginator(reply, 10)    #this paginate only 10 reply per page
    page_number = request.GET.get('page')
    reply = paginator.get_page(page_number)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        form.instance.reply_post = post
        if form.is_valid():
            form.save()
            form = ReplyForm()
            messages.info(request, f'Comment added successfully')
            return redirect('detail', pk=post.id)
    context = {'post': post, 'reply': reply, 'form':form, 'total_reply':total_reply}
    return render(request, 'blog/postdetail.html', context)

@login_required(login_url = 'login')    #this decorator restrict user from updating post before login
def updatepost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post) #show post that you want to edit
    if request.method =='POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.info(request, f'Post updated successfully')
                return redirect('detail', pk=post.id)
    context = {'form': form}
    return render(request, 'blog/update.html', context)

@login_required(login_url = 'login')    #this decorator restrict user from deleting post before login
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method =='POST':
        post.delete()
        messages.info(request, f'Post has been deleted successfuly')
        return redirect('home')
    context = {'post': post}
    return render(request, 'blog/delete.html', context)

#user profile
@login_required(login_url = 'login')
def profile(request):
    context = {}
    return render(request, 'blog/profile.html', context)


#updating profile
@login_required(login_url = 'login')
def update_profile(request):
    form = UpdateProfileForm(instance=request.user)     #user infomation (username,email...)
    p_form = UpdatePicture(instance=request.user.profile)   #profile picture
    if request.method =='POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        p_form = UpdatePicture(request.POST, request.FILES, instance=request.user.profile)
        p_form.instance.user = request.user
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            messages.info(request, f'Profile updated successfull')
            return redirect('profile')
    context = {'form':form, 'p_form':p_form}
    return render(request, 'blog/update_profile.html', context)


#delete a reply comment
@login_required(login_url = 'login')
def delete_reply(request,pk):
    reply = Reply.objects.get(id=pk)
    if request.method =='POST':
        reply.delete()
        messages.info(request, f'Comment has been deleted successfuly')
        return HttpResponse("Comment deleted successfull")
