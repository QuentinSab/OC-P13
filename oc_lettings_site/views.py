"""
Views for the oc_lettings_site application.
"""

from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
def index(request):
    """
    Render the home page.
    """
    logger.info("Index page accessed")

    return render(request, 'index.html')


def error_404(request, exception):
    """
    Render the custom 404 page.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Render the custom 500 page.
    """
    return render(request, '500.html', status=500)
