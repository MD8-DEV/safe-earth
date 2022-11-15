from django.contrib import admin
from django.urls import path, include
from user_auth.views import Dashboard
from chat.views import Chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("user_auth.urls")),
    path('chat/<str:username>', Chat.as_view()),
    path('', Dashboard.as_view())
]
