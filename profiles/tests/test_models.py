"""
Tests for the models from the profiles.
"""

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation():
    """
    Check that a profile can be created and linked to a user.
    """
    user = User.objects.create_user(username="test_user", password="mdp123")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert profile.user == user
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_str_method():
    """
    Check that the string representation returns the username.
    """
    user = User.objects.create_user(username="jean", password="mdp123")
    profile = Profile.objects.create(user=user)

    assert str(profile) == "jean"


@pytest.mark.django_db
def test_profile_favorite_city_blank():
    """
    Check that favorite_city can be left blank.
    """
    user = User.objects.create_user(username="paul", password="mdp123")
    profile = Profile.objects.create(user=user)

    assert profile.favorite_city == ""
