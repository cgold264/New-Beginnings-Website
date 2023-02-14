# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    template = loader.get_template('NewBeginnings/index.html')
    return HttpResponse(template.render(context, request))
