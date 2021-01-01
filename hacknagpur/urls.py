from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogs.urls')),
    path('schedule/', include('schedule.urls')),
    path('', include('accounts.urls')),
    path('chat/', include('chat.urls')),
]
