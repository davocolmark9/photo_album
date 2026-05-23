from django.urls import path
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
]