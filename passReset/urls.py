from .views import ChangePasswordView
from django.urls import path,include

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]