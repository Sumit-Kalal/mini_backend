from django.urls import path
from .views import home_view, register_api
from . import views
from myapp.views import test_api
urlpatterns = [
    path("api/register/", register_api, name="register_api"),
    path("login/", views.login_view, name="login_form"),
    path("dashboard/", home_view, name="dashboard"),
    path('users/', views.user_list, name='user_list'),
    path('entries/edit/<int:id>/', views.edit_entry, name='edit_entry'),
    path('entries/delete/<int:id>/', views.delete_entry, name='delete_entry'),
    path("test/", test_api),
    path("", register_api, name="register_api"),
]
