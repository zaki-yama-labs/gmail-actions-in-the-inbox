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
from .forms import MovieForm


logger = logging.getLogger(__name__)


class MovieListView(View):
	template_name = 'movie_list.html'

	def get(self, request):
		template_values = {
				'movies': Movie.query(),
				}

		return render(request, self.template_name, template_values)

	def post(self, request):
		title = request.POST.get('title')
		movie = Movie(title=title)
		movie.put()

		return redirect('go_to_action:movie_list')


class NewMovieView(View):
	template_name = 'movie_edit.html'

	def get(self, request):
		form = MovieForm()
		template_values = {
				'app_name': request.resolver_match.app_name,
				'form': form,
				}

		return render(request, self.template_name, template_values)


class MovieDetailView(View):
	template_name = 'movie_detail.html'

	def get(self, request, pk=None):
		template_values = {
				'movie': Movie.get_by_id(int(pk)),
				}

		return render(request, self.template_name, template_values)

