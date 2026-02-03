
from django.urls import path
from .views import login_view, register_view, dashboard
from django.contrib.auth import views as auth_views
urlpatterns = [
 path('', login_view, name='login'),
 path('register/', register_view, name='register'),
 path('dashboard/', dashboard, name='dashboard'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


