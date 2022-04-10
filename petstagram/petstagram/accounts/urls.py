from django.urls import path, reverse_lazy
from django.views import generic as views

from petstagram.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, ChangeUserPasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('profile/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/create/', UserRegisterView.as_view(), name='create profile'),
    # path('profile/edit/', EditProfileView, name='edit profile'),
    # path('profile/delete/', DeleteProfileView, name='delete profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done', views.RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done')
)