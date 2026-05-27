"""
Tests for the views from the profiles.
"""

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    Check that profiles index page returns 200 and uses correct template.
    """
    user = User.objects.create_user(username="jean", password="mdp123")
    Profile.objects.create(user=user, favorite_city="Paris")

    response = client.get(reverse("profiles:index"))

    assert response.status_code == 200
    assert "profiles/index.html" in [template.name for template in response.templates]
    assert user.profile in response.context["profiles_list"]


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Check that profile detail page returns 200 and displays correct profile.
    """
    user = User.objects.create_user(username="paul", password="mdp123")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    response = client.get(
        reverse("profiles:profile", args=[user.username])
    )

    assert response.status_code == 200
    assert "profiles/profile.html" in [template.name for template in response.templates]
    assert response.context["profile"] == profile
