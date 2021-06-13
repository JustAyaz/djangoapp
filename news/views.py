from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from .models import *
from .forms import *


def index(request):
    form = LinkForm()
    return render(request, 'news/index.html', context={'form': form})


class LinkCreate(View):

    def get(self, request):
        form = LinkForm
        return render(request, 'news/index.html', context={'form': form})

    def post(self, request):
        bound_form = LinkForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()

        return render(request, 'news/index.html', context={'form': bound_form})


def lib(request):
    links = Links.objects.all()
    return render(request, 'news/lib.html', context={'links' : links})
