"""
Test for the Django admin modifications.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import Client


class AdminSiteTests(TestCase):
    """Tests for the Admin site."""

    def setUp(self) -> None:
        """Setup function to create an admin and an user account."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="testpass123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass123",
            name="Test User"
        )

    def test_users_list(self) -> None:
        """Test that users are listed on the page."""
        users_page_url = reverse('admin:core_customuser_changelist')
        res = self.client.get(users_page_url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self) -> None:
        """Test that check if the user page loads."""
        user_page_url = reverse(
            'admin:core_customuser_change',
            args=[self.user.id]
            )
        res = self.client.get(user_page_url)
        self.assertEqual(res.status_code, 200)

    def test_user_add(self) -> None:
        """Test for adding a user"""
        user_add_url = reverse('admin:core_customuser_add')
        res = self.client.get(user_add_url)
        self.assertEqual(res.status_code, 200)
