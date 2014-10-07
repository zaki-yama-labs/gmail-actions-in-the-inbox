# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import MovieListView

urlpatterns = patterns('',
    (r'^movies/new/$', NewMovieView.as_view()),
    (r'^movies/(?P<movie_id>\d+)/$', MovieView.as_view()),
	url(r'^movies/$', MovieListView.as_view(), name='movie_list'),
)
