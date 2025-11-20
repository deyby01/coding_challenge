from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/<str:username>/', views.ProfileDetailView.as_view(), name='profile'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles'),
]
