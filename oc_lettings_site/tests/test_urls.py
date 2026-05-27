"""
Tests for the urls from the oc_lettings_site application.
"""

from django.urls import reverse, resolve
from oc_lettings_site import views


def test_home_url():
    """
    Check that home URL resolves to "/" and maps to index view.
    """
    path = reverse("index")
    assert path == "/"
    assert resolve(path).func == views.index


def test_admin_url():
    """
    Check that admin URL is correctly configured at "/admin/".
    """
    path = reverse("admin:index")
    assert path == "/admin/"


def test_lettings_include():
    """
    Check that lettings URLs are correctly namespaced under "/lettings/".
    """
    path = reverse("lettings:index")
    assert path == "/lettings/"


def test_profiles_include():
    """
    Check that profiles URLs are correctly namespaced under "/profiles/".
    """
    path = reverse("profiles:index")
    assert path == "/profiles/"
