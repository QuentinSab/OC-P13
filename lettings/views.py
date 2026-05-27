"""
Views for the lettings application.
"""

from django.shortcuts import render
from .models import Letting

import logging

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
def index(request):
    """
    Display the list of available lettings.
    """
    logger.info("Lettings index page accessed")

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
def letting(request, letting_id):
    """
    Display details for a specific letting.
    """
    logger.info(f"Letting page requested for id: {letting_id}")

    try:
        letting = Letting.objects.get(id=letting_id)

    except Letting.DoesNotExist:
        logger.error(f"Letting not found: {letting_id}")
        raise

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
