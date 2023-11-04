
from django.contrib import admin
from django.urls import path,include
from .views import DashboardView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
      path('', DashboardView.as_view(), name='dashboard'),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
