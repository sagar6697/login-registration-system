from django.contrib import admin
from django.urls import path,include
from . import views
from .views import CustomPasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from app1.views import signin


urlpatterns = [
    path('',views.home ,name='home'),
    path('signup',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout',views.signout ,name='signout'),
    path('index',views.index ,name='index'),
    path('signouthome',views.signouthome ,name='signouthome'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_done'),
    path('accounts/login/', signin, name='accounts_login'),
]
