from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
import os
from django.conf import settings

from core.models import User


class HomeView(TemplateView):
    """
    Home page view - accessible to everyone.
    Shows a welcome message and login status.
    """
    template_name = 'core/home.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    User profile view - requires authentication.
    Displays any user's information based on the username parameter.
    """
    model = User
    template_name = 'core/profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.request.user.username == self.object.username

        drawing_path = settings.BASE_DIR / 'static' / 'image' / 'drawing'
        image_files = []
        if drawing_path.exists():
            for name in drawing_path.iterdir():
                if name.suffix.lower() in {'.jpg', '.jpeg', '.png'}:
                    image_files.append(f"image/drawing/{name.name}")

        context['drawing_images'] = image_files

        
        return context


class ProfileListView(LoginRequiredMixin, ListView):
    """
    Profiles list view - requires authentication.
    Displays a list of all users.
    """
    model = User
    template_name = 'core/profiles.html'
    context_object_name = 'users'
    