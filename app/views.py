from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Photo

def index(request):
    photos=Photo.objects.all().order_by('-created_at')
    return render(request,'app/index.html',{'photos':photos})

def users_detail(request,pk):
    user=get_object_or_404(User,pk=pk)
    photos=user.photo_set.all().order_by('-created_at')
    return render(request,'app/users_detail.html',{'user':user,'photos':photos})

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            input_username=form.cleaned_data['username']
            input_password=form.cleaned_data['password']
            #フォームの入力値で認証できれば、ユーザーオブジェクト、できなければNONE
            new_user=authenticate(username=input_username,password=input_password)
            #認証時のみユーザーをログインさせる
            if new_user is not None:
                #loginmethodは、認証できていなくてもログインできる。（上のauthenticateで認証を実行。）
                login(request,new_user)
            return redirect('app:user_detail',pk=new_user.pk)
    else:
        form=UserCreationForm()
    return render(request,'app/signup.html',{'form':form})
    