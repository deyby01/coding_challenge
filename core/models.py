from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    """

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='image/user/', blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return super().get_full_name() or self.username

    def get_profile_picture_path(self):
        """
        Return the path to the profile picture in static/image/user/.
        Checks for common image extensions (jpg, jpeg, png).
        Returns None if no image is found.
        """
        import os
        from django.conf import settings
        
        base_path = settings.BASE_DIR / 'static' / 'image' / 'user'
        extensions = ['jpg', 'jpeg', 'png']
        
        for ext in extensions:
            image_path = base_path / f'{self.username}.{ext}'
            if image_path.exists():
                return f'image/user/{self.username}.{ext}'
        
        return None
