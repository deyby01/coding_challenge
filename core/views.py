from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from core.models import User


def home(request):
    """
    Home page view - accessible to everyone.
    Shows a welcome message and login status.
    """
    return render(request, 'core/home.html')


@login_required
def profile(request, username):
    """
    User profile view - requires authentication.
    Displays any user's information based on the username parameter.
    """
    user = get_object_or_404(User, username=username)
    profile_picture = user.profile_picture
    return render(request, 'core/profile.html', {
        'user': user,
        'is_own_profile': request.user.username == username,
        'profile_picture': profile_picture,
        'description': user.description,
        'gender': user.gender,
    })


@login_required
def profiles(request):
    """
    Profiles list view - requires authentication.
    Displays a list of all users.
    """
    users = User.objects.all().order_by('username')
    profile_pictures = [user.profile_picture for user in users]
    return render(request, 'core/profiles.html', {
        'users': users,
        'profile_pictures': profile_pictures
    })
