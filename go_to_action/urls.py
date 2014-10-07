# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import MovieListView, NewMovieView, MovieDetailView, EmailSenderView

urlpatterns = patterns('',
	url(r'^movies/$', MovieListView.as_view(), name='movie_list'),
	url(r'^movies/new/$', NewMovieView.as_view(), name='movie_new'),
	url(r'^movies/(?P<pk>\d+)/$', MovieDetailView.as_view(), name='movie_detail'),
)
