from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def register_views(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to dashboard after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_views(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_views(request):
    user_profile = request.user.profile  # Assuming you have a one-to-one relationship with Profile
    return render(request, 'dashboard.html', {'user_profile': user_profile})
