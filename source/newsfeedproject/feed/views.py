from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Novelty

def feed(request):
    noveltys = Novelty.objects.all().order_by('published_date')
    return render(request, 'feed/index.html', {'noveltys':noveltys})

def novelty_detail(request, pk):
    novelty = get_object_or_404(Novelty, pk=pk)
    return render(request, 'feed/detail.html', {'novelty':novelty})
