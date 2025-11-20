from django.test import TestCase
from django.urls import reverse

from core.models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)


class ProfilesListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profiles_list_view(self):
        response = self.client.get(reverse('core:profiles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profiles.html')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Photo')

    
class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_detail_view(self):
        response = self.client.get(reverse('core:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile.html')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Basic Information')
        self.assertContains(response, 'Account Details')
        self.assertContains(response, 'img')
        self.assertContains(response, 'Back to Profiles')
        self.assertContains(response, 'modal-content')