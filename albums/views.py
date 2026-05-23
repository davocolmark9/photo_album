from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from .models import Album, Photo
from .mixins import OwnerRequiredMixin
from .forms import SignUpForm, PhotoForm


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.album = get_object_or_404(Album, pk=kwargs['album_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.album = self.album
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.album.pk})


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'albums/signup.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Album.objects.all()
        return Album.objects.filter(owner=self.request.user)


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')


class AlbumDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')


from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')