from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm

@login_required(login_url=reverse_lazy('profile'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('main-page')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь "
                                                            "не найден"})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user = authenticate(username=new_user.username,
                                    password=request.POST['password1'])
            login(request, user=new_user)
            return redirect(reverse('profile'))
    else:
        user_form = ExtendedUserCreationForm()
    context = {'form': user_form}
    return render(request, 'app_auth/register.html', context)
