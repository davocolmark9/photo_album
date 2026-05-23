from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import (
    SignUpView,
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    PhotoUploadView,
)

urlpatterns = [
    path('', AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('create/', AlbumCreateView.as_view(), name='album_create'),
    path('update/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('delete/<int:pk>/', AlbumDeleteView.as_view(), name='album_delete'),
    path('album/<int:album_pk>/upload/', PhotoUploadView.as_view(), name='photo_upload'),
    
    # Auth URLs
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='albums/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='album_list'), name='logout'),
]