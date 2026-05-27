"""
Tests for the urls from the profiless.
"""

from django.urls import reverse, resolve

from profiles import views


def test_profiles_index_url():
    """
    Check that profiles index URL resolves to the index view.
    """
    url = reverse("profiles:index")

    assert resolve(url).func == views.index


def test_profile_detail_url():
    """
    Check that profile detail URL resolves to the profile view.
    """
    url = reverse("profiles:profile", args=["jean"])

    assert resolve(url).func == views.profile
