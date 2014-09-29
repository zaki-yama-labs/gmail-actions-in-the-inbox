# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from .views import MovieListView, NewMovieView, MovieView

urlpatterns = patterns('',
    (r'^movies/$', MovieListView.as_view()),
    (r'^movies/new/$', NewMovieView.as_view()),
    (r'^movies/(?P<movie_id>\d+)/$', MovieView.as_view()),
)
