from django.urls import path
from tech.api import views

urlpatterns = [
    path('settings/', views.SettingsListAPIView.as_view(), name="settings")
]