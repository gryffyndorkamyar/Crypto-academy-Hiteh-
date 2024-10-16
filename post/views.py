from django.shortcuts import render
from django.contrib.auth.models import User
#from shop.models import Product, Category, UserProfile
from django.shortcuts import render, get_object_or_404
#from .models import Product, Category
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Product , UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import UpdateUserForm, UpdateProfileForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
#from .forms import ComplaintForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from post import forms
from . import forms
from post.forms import UpdateUserForm, UpdateProfileForm, ComplaintForm
import requests


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def mag(request):
    return render(request, 'mag.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, is_approved=False)
            auth_login(request, user)
            messages.info(request, 'Welcome To Your Crypto Blog')
            return redirect('index')
    return render(request, 'Signup.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # استفاده از نام جدید برای تابع login
                return redirect('index')  # یا هر صفحه‌ای که می‌خواهید کاربر به آن هدایت شود
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
        else:
            messages.error(request, "Invalid form submission.")
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def EditProfile(request):
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile has been updated!.')
                return redirect('profile')
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, 'editprofile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def EditPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # مهم! برای جلوگیری از خروج کاربر پس از تغییر رمز عبور
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': form})


def ticket(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            complaint = form.cleaned_data.get('complaint')

            send_mail(
                'your ticket',
                f'name: {name}\nemail: {email}\n\nticket:\n{complaint}',
                'your_email@example.com',  # ایمیل فرستنده
                ['grifindorekamyar@gmail.com'],  # ایمیل ادمین
                fail_silently=False,
            )
            return redirect('complaint_success')
    else:
        form = ComplaintForm()

    return render(request, 'ticket.html', {'form': form})


def cart(request):
    pass


def cryptoprice(request):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,tether',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    context = {
        'bitcoin_price': data['bitcoin']['usd'],
        'ethereum_price': data['ethereum']['usd'],
        'tether_price': data['tether']['usd']
    }
    return render(request, 'cryptoprice.html', context)

@staff_member_required
def approve_users(request):
    users = User.objects.filter(userprofile__is_approved=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = User.objects.get(id=user_id)
        if action == 'approve':
            user.userprofile.is_approved = True
            user.userprofile.save()
        elif action == 'reject':
            user.delete()
        return redirect('approve_users')
    return render(request, 'approve_users.html', {'users': users})


def profile(request):
    return render(request , 'profile.html')




