# -*- coding: utf-8 -*-
from django import forms
from .models import Movie

class MovieForm(forms.Form):
	u'''映画'''
	title = forms.CharField(required=True)
