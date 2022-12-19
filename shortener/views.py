import pyshorteners

from django.shortcuts import render


def short(request):
    return render(request, 'shortener/shortener.html')


def short_link(request):
    link = request.GET.get('url')
    shortener = pyshorteners.Shortener()
    short_link = shortener.tinyurl.short(link)
    return render(request, 'shortener/shorted_link.html', {'short_link': short_link})
