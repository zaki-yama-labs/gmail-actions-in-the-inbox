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

from . import APP_LABEL
from .models import Movie
from .forms import MovieForm


logger = logging.getLogger(__name__)


class EmailSenderView(View):
	template_name = APP_LABEL + '/send_mail.html'

	def get(self, request, pk=None):
		# require users to be logged in to send emails
		user = users.get_current_user()
		if not user:
			return redirect(users.create_login_url(request.path))

		obj = Movie.get_by_id(int(pk))
		logger.warn(pk)
		if not obj:
			return redirect('go_to_action:movie_list')

		email = user.email()
		logger.warn(request.path)

		# the review url corresponds to the App Engine app url
		pr = urlparse(request.build_absolute_uri())
		app_name = request.resolver_match.app_name
		url = '%s://%s/%s' % (pr.scheme, pr.netloc, app_name)

		# load the email template and replace the placeholder with the review url
		template_values = {
				'url': url,
				'pk': pk,
				'title': obj.title,
				}
		email_body = loader.render_to_string(APP_LABEL + '/mail_template.html', Context(template_values))

		message = mail.EmailMessage(
				sender=email,
				to=email,
				subject='See the detail of movie \'%s\'' % obj.title,
				html=email_body)
		template_values = {
				'email': email,
				}

		try:
			message.send()
			return render(request, self.template_name, template_values)
		except:
			return HttpResponseServerError()


class MovieListView(View):
	template_name = APP_LABEL + '/movie_list.html'

	def get(self, request):
		template_values = {
				'movies': Movie.query(),
				}

		return render(request, self.template_name, template_values)

	def post(self, request):
		title = request.POST.get('title')
		movie = Movie(title=title)
		movie.put()

		template_values = {
				'movies': Movie.query(),
				}
		return render(request, self.template_name, template_values)


class NewMovieView(View):
	template_name = APP_LABEL + '/movie_edit.html'

	def get(self, request):
		form = MovieForm()
		template_values = {
				'app_name': request.resolver_match.app_name,
				'form': form,
				}

		return render(request, self.template_name, template_values)


class MovieDetailView(View):
	template_name = APP_LABEL + '/movie_detail.html'

	def get(self, request, pk=None):
		template_values = {
				'movie': Movie.get_by_id(int(pk)),
				}

		return render(request, self.template_name, template_values)
