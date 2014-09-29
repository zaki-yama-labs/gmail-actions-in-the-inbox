# -*- coding: utf-8 -*-
import logging
from urlparse import urlparse

from google.appengine.api import mail
from google.appengine.api import users

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from .models import Movie


logger = logging.getLogger(__name__)


class MovieListView(View):

	def get(self, request):
		return HttpResponse('heeelo')


class NewMovieView(View):

	def get(self, request):
		return HttpResponse('heeelo')


class MovieView(View):

	def get(self, request):
		return HttpResponse('heeelo')
