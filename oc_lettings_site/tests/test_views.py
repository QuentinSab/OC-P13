"""
Tests for the views from the oc_lettings_site application.
"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Check that home page returns 200 and uses correct template.
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "index.html" in [template.name for template in response.templates]


@pytest.mark.django_db
def test_error_404_view(client):
    """
    Check that custom 404 page returns 404 status code.
    """
    response = client.get("/not_existing/")
    assert response.status_code == 404
    assert "404.html" in [template.name for template in response.templates]
