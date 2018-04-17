from django.urls import path

from . import views

urlpatterns = [
    path('<project_name>/getBuildVersion', views.get_build_version, name='get_build_version'),
    path('<project_name>/getReleaseVersion', views.get_release_version, name='get_release_version'),
    path('<project_name>/incrementVersion', views.increment_version, name='increment_version'),
]
