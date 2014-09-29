# -*- coding: utf-8 -*-
from google.appengine.ext import ndb


class Movie(ndb.Model):
	title = ndb.StringProperty(required=True, default='No Title')
