from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from astrosite.accounts.forms import RegisterForm, LoginForm, ProfileUpdateForm
from astrosite.accounts.models import Profile


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)



            return redirect('home')


    return render(request, 'accounts/logout.html')







@login_required
def profile_view(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)


    has_profile_details = any([
        profile.first_name,
        profile.last_name,
        profile.date_of_birth
    ])

    context = {
        'user': request.user,
        'profile': profile,
        'has_profile_details': has_profile_details,
    }
    return render(request, 'accounts/profile.html', context)
@login_required
def edit_profile_view(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)




class ChangePasswordView(PasswordChangeView):

    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')

@login_required
def delete_profile_view(request):

    if request.method == 'POST':
        try:
            profile = request.user.profile
            user = request.user
            profile.delete()
            user.delete()

            return redirect('home')
        except Profile.DoesNotExist:

            return redirect('profile')

    return render(request, 'accounts/delete_profile.html')
