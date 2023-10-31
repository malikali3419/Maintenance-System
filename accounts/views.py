from django.views import View
from django.shortcuts import render, redirect
from .models import User


class UserLoginView(View):
    template_name = 'accounts/login.html'
    def get(self, request):
        # Your logic for handling GET requests
        return render(request, self.template_name)