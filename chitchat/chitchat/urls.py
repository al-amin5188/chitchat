
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authuser.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('posts/', include('posts.urls')),
    path('notification/', include('notification.urls')),

]
