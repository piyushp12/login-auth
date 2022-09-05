from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from base.views import *



urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('signup/',signup.as_view(),name='signup'),
    # path('signin/',views.signin,name='signin'),
    # path('login/',views.login,name='login'),
    # path('page/',views.page,name='page')

    # path("", HomeView.as_view(), name="home"),
    path("dashboard",DashboardView.as_view(),name="dashboard"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("forgot-password", ForgotPasswordView.as_view(), name="forgot-password"),
    path("verify-otp", VerifyOTPView.as_view(), name="verify-otp"),
    path("set-password", SetPasswordView.as_view(), name="set-password"),
    path('main/',MainView.as_view(), name="main")

]