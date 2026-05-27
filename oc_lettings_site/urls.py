"""
URL configuration for the oc_lettings_site project.
"""

from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'
