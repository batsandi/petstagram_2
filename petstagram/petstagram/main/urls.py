from django.urls import path

from petstagram.main.views.generic import DashboardView, HomeView
from petstagram.main.views.pet_photos import show_pet_photo_details, CreatePetPhotoView, edit_pet_photo, like_pet_photo, \
    PetPhotoDetailsView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
)
