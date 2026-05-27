"""
Views for the profiles application.
"""

from django.shortcuts import render
from .models import Profile

import logging

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo.
def index(request):
    """
    Display the list of user profiles.
    """
    logger.info("Profiles index page accessed")

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
def profile(request, username):
    """
    Display details for a specific user profile.
    """
    logger.info(f"Profile page requested for user: {username}")

    try:
        profile = Profile.objects.get(user__username=username)

    except Profile.DoesNotExist:
        logger.error(f"Profile not found: {username}")
        raise

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
