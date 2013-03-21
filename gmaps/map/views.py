from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.

# def login(request):
    
