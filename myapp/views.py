from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm, RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login_form')
    else:
        form = RegisterForm()
    return render(request, 'myapp/Registration_form.html', {'form': form})


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "myapp/login_form.html", {
                "error": "Invalid credentials"
            })

    return render(request, "myapp/login_form.html")


def home_view(request):
    return render(request, "myapp/dashboard.html")

from django.shortcuts import get_object_or_404, redirect

from .forms import EntryForm
from django.shortcuts import get_object_or_404, redirect, render

def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id, user=request.user)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = EntryForm(instance=entry)

    return render(request, 'myapp/edit_entry.html', {'form': form})

def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id, user=request.user)

    if request.method == "POST":
        entry.delete()

    return redirect('user_list')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})