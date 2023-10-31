from django.views import View
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        error_message = 'Invalid username or password. Please try again.'
        messages.error(request, error_message)
        return render(request, self.template_name)
    

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')