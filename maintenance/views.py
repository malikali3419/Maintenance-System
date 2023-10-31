from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import View

User = get_user_model()

class DashboardView(LoginRequiredMixin, View):
    template_name = 'maintenance/dashboard.html'
    def get(self, request):
        user = request.user
        return render(request, self.template_name)