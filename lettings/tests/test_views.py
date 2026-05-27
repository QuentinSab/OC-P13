"""
Tests for the views from the lettings.
"""

import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    Check that lettings index view returns correct response.
    """
    address = Address.objects.create(
        number=10,
        street="Avenue du maréchal Foch",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )

    Letting.objects.create(
        title="Test annonce",
        address=address,
    )

    response = client.get(reverse("lettings:index"))

    assert response.status_code == 200

    templates = [template.name for template in response.templates]
    assert "lettings/index.html" in templates

    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 1


@pytest.mark.django_db
def test_letting_detail_view(client):
    """
    Check that letting detail view returns correct response.
    """
    address = Address.objects.create(
        number=10,
        street="Avenue du maréchal Foch",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )

    letting = Letting.objects.create(
        title="Test annonce",
        address=address,
    )

    response = client.get(
        reverse("lettings:letting", args=[letting.id])
    )

    assert response.status_code == 200

    templates = [template.name for template in response.templates]
    assert "lettings/letting.html" in templates

    assert response.context["title"] == "Test annonce"
    assert response.context["address"] == address
