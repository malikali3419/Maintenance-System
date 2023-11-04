from django.contrib import admin
from .models import User

admin.site.register(User)
admin.site.site_title = 'Felgenkosmetik'
admin.site.site_header = 'Felgenkosmetik'
admin.site.index_title = 'Felgenkosmetik'
