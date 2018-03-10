from django.http import HttpResponse
from versionControl.models import Version
from django.views.decorators.csrf import csrf_exempt


def get_version(project):
    major = project.major_version
    minor = project.minor_version
    hotfix = project.hotfix_version
    build = project.build_version
    return major, minor, hotfix, build


def increment(version_type, project):
    if version_type == "major":
        project.major_version = project.major_version+1
        project.minor_version = 0
        project.hotfix_version = 0
        project.build_version = 0
    elif version_type == "minor":
        project.minor_version = project.minor_version+1
        project.hotfix_version = 0
        project.build_version = 0
    elif version_type == "hotfix":
        project.hotfix_version = project.hotfix_version+1
        project.build_version = 0
    elif version_type == "build":
        if project.build_version == 999:
            project.build_version = 0
        else:
            project.build_version = project.build_version+1
    project.save()
    return project


def get_build_version(request, project_name):
    project = Version.objects.get(project_name=project_name)
    major, minor, hotfix, build = get_version(project)
    version = "{0}.{1}.{2}.b{3}".format(major, minor, hotfix, str(build).zfill(3))
    return HttpResponse(version)


def get_release_version(request, project_name):
    project = Version.objects.get(project_name=project_name)
    major, minor, hotfix, build = get_version(project)
    release_version = "{0}.{1}.{2}".format(major, minor, hotfix)
    return HttpResponse(release_version)


@csrf_exempt
def increment_version(request, project_name):
    version_type = request.POST["version_type"]
    project = Version.objects.get(project_name=project_name)
    project = increment(version_type, project)
    return HttpResponse(project.minor_version)
