from django.contrib import admin
from django.urls import path, include
from user_auth.views import Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("user_auth.urls")),
    path('', Dashboard.as_view())
]
