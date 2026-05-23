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
from .models import Album, Photo  # ← Make sure Photo is imported
from .mixins import OwnerRequiredMixin
from .forms import SignUpForm, PhotoForm  # ← Make sure PhotoForm is imported


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


# ... rest of your views (AlbumListView, etc.) stay the same