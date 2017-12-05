# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'quotation/index.html'


class Form(TemplateView):
    template_name = 'form/form.html'
