"""
Tests for the models from the lettings.
"""

import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    """
    Check that Address string returns number and street.
    """
    address = Address.objects.create(
        number=9,
        street="Avenue du maréchal Foch",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )

    assert str(address) == "9 Avenue du maréchal Foch"


@pytest.mark.django_db
def test_address_verbose_name_plural():
    """
    Check that Address plural name is correctly defined.
    """
    assert Address._meta.verbose_name_plural == "Addresses"


@pytest.mark.django_db
def test_letting_str():
    """
    Check that Letting string returns the title.
    """
    address = Address.objects.create(
        number=9,
        street="Avenue du maréchal Foch",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )

    letting = Letting.objects.create(
        title="Appartement charmant",
        address=address,
    )

    assert str(letting) == "Appartement charmant"
