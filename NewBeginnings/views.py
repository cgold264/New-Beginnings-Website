# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req, 'index.html')

def home(req):
    return render(req, 'index.html')

# Create your views here.
