"""
Tests for the urls from the lettings.
"""

from django.urls import reverse, resolve

from lettings import views


def test_lettings_index_url():
    """
    Check that lettings index URL resolves correctly.
    """
    url = reverse("lettings:index")
    assert url == "/lettings/"
    assert resolve(url).func == views.index


def test_letting_detail_url():
    """
    Check that letting detail URL resolves correctly.
    """
    url = reverse("lettings:letting", args=[3])
    assert url == "/lettings/3/"
    assert resolve(url).func == views.letting
