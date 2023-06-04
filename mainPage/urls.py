from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHomePage, name='getHomePage'),
    path('about/', views.getAboutPage),
    path('contacts/', views.getContactsPage),
    path('addQuestion/', views.addQuestion)
]