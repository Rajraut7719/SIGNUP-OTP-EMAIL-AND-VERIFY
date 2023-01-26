
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegisterAPI.as_view()),
    path('verity-otp/',views.VerifyOTP.as_view())
]
