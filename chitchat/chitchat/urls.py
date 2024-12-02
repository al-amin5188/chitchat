
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authuser.urls')),
    path('home/', include('home.urls')),
    path('resource/', include('resource.urls')),
    path('messages/', include('user_messages.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    path('notification/', include('notification.urls')),
    
]