# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import MovieListView, NewMovieView, MovieDetailView, EmailSenderView

urlpatterns = patterns('',
	url(r'^new/$', NewMovieView.as_view(), name='movie_new'),
	url(r'^(?P<pk>\d+)/$', MovieDetailView.as_view(), name='movie_detail'),
	url(r'^(?P<pk>\d+)/edit/$', NewMovieView.as_view(), name='movie_edit'),
	url(r'^(?P<pk>\d+)/email/$', EmailSenderView.as_view(), name='send_email'),
	url(r'^', MovieListView.as_view(), name='movie_list'),
)
