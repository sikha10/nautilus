from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username}!")
            return redirect('user-signin')

        elif User.objects.filter(username=username):
            messages.error(request, f"Username already in use")
        else:
            messages.error(request, f"check password or email")
    else:
        form = UserRegisterForm()
    return render(request, 'sign_up.html', {"form": form})

