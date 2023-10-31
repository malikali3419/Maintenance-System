
from django.contrib import admin
from django.urls import path,include
from .views import UserLoginView, LogoutView

urlpatterns = [
      path('login/', UserLoginView.as_view(), name='login'),
      path('logout/', LogoutView.as_view(), name='logout'),
]
