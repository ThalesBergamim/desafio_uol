from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('list/', views.ListView.as_view(), name='list'),
]
