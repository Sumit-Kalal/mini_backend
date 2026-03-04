from django.urls import path
from .views import   register, home_view
from . import views
from myapp.views import test_api
urlpatterns = [
    path("register/", register, name="Registration_form"),
    path("login/", views.login_view, name="login_form"),
    path("dashboard/", home_view, name="dashboard"),
    path('users/', views.user_list, name='user_list'),
    path('entries/edit/<int:id>/', views.edit_entry, name='edit_entry'),
    path('entries/delete/<int:id>/', views.delete_entry, name='delete_entry'),
    path("test/", test_api, name="test_api"),
    path("", register, name="Registration_form"),
]
