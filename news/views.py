from django.shortcuts import render, redirect
from django.views.generic import View

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
    links = Links.objects.order_by('-created_at')

    return render(request, 'news/lib2.html', context={'links': links})


def deleteOrder(request, pk):
    link = Links.objects.get(id=pk)
    if request.method == "POST":
        link.delete()
        return redirect('/all/')
    context = {'link': link}
    return render(request, 'news/delete.html', context)


def openLink(request, key):
    link = Links.objects.get(my_link=key)
    actual_link = link.link
    print(key, actual_link)
    return redirect(actual_link)
