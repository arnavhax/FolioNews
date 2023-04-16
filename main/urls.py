from django.urls import path

from . import views
from .views import SignUpView
from .views import MyLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main/', views.main, name="main"),
    path('saveStock/', views.saveStock, name="saveStock"),
    path('update/', views.update, name="update"),
    path('register/', SignUpView.as_view(), name='register'),
    path('', MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<str:name>/', views.delete, name='delete'),
]