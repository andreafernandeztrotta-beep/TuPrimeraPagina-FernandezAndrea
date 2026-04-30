from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # ESTO TIENE QUE DECIR .urls
    path('', include('app_akku.urls')),
]


