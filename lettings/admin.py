"""
Admin configuration for the lettings application.
"""

from django.contrib import admin

from lettings.models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
