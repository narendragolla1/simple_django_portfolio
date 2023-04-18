from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    context={
        "NAME":settings.DATA["NAME"]
    }
    return render(request,'main/index.html',context)
def project(request):
    context={
        "PROJECTS":settings.DATA["PROJECT"]
    }
    return render(request,'main/project.html',context)

def languages(request):
    context={
        "LANGUAGES":settings.DATA["LANGUAGES"]
    }
    return render(request,'main/languages.html',context)

    