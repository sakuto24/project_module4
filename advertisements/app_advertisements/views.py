from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisement(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    return render(request, 'advertisement.html')



