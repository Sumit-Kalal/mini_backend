from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login 

@csrf_exempt    
def register_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return JsonResponse({"error": "Missing fields"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)



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

@csrf_exempt
def test_api(request):
    return JsonResponse({'message': "Backend connected successfully!"})
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]