from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
)

urlpatterns = [
    path('', AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('create/', AlbumCreateView.as_view(), name='album_create'),
    path('update/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('delete/<int:pk>/', AlbumDeleteView.as_view(), name='album_delete'),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='albums/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]