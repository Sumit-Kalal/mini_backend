from django.urls import path
from .views import home_view, register_api, UserViewSet
from . import views
from myapp.views import test_api
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("api/register/", register_api, name="register_api"),
    path("api/login/", views.login_view, name="login_api"),
    path("dashboard/", home_view, name="dashboard"),
    path('users/', views.user_list, name='user_list'),
    path('entries/edit/<int:id>/', views.edit_entry, name='edit_entry'),
    path('entries/delete/<int:id>/', views.delete_entry, name='delete_entry'),
    path("test/", test_api),
    path("", register_api, name="register_api"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
