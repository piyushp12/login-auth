from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup
from django.views import View
from django.contrib.auth import authenticate,login,logout


class HomeView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        params = request.POST
        user = authenticate(
            phone_number=params["phone"], password=params["password"])
        if user is not None and user.user_type == "Admin":
            login(request, user)
            return redirect("app:main")
        elif user is not None and user.user_type == "Farm":
            login(request, user)
            return redirect("farm:dashboard")
        elif user is not None and user.user_type == "Group":
            login(request, user)
            return redirect("group:dashboard")
        elif user is not None and user.user_type == "Staff":
            login(request, user)
            return redirect("staff:dashboard")
        else:
            return redirect("app:home")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("app:home")


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, "common/forgot-password.html")

    def post(self, request):
        return redirect("app:verify-otp")


class VerifyOTPView(View):
    def get(self, request):
        return render(request, "common/otp-verify.html")

    def post(self, request):
        return redirect("app:set-password")


class SetPasswordView(View):
    def get(self, request):
        return render(request, "common/set-password.html")

    def post(self, request):
        return redirect("app:home")


class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")


class MainView(View):
    def get(self, request):
        return render(request, "main.html")


# def index(request):
#     return render(request, 'index.html')
class signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name')
            last = request.POST.get('last')
            user = request.POST.get('user')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm = request.POST.get('confirm')
            Address = request.POST.get('Address')
            print(name, last, user, email, phone, password, confirm, Address)
            Signup(name=name, last=last, user=user, email=email, phone=phone,
                   password=password, confirm=confirm, Address=Address).save()

        return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')

def page(request):
    return render(request, 'page.html')

def login(request):
    return render(request, 'login.html')
