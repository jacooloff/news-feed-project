from django.shortcuts import render
from django.utils import timezone
from .models import Novelty

def feed(request):
    noveltys = Novelty.objects.all().order_by('published_date')
    return render(request, 'feed/index.html', {'noveltys':noveltys})
