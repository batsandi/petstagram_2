from django.urls import path

from petstagram.accounts.views import UserRegisterView

urlpatterns = (
    path('login/', UserRegisterView.as_view(), name='login user'),
)