from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Novelty
from .forms import NoveltyForm, NoveltyFormForEdit

def feed(request):
    noveltys = Novelty.objects.all().order_by('published_date')
    return render(request, 'feed/index.html', {'noveltys':noveltys})

def novelty_detail(request, pk):
    novelty = get_object_or_404(Novelty, pk=pk)
    return render(request, 'feed/detail.html', {'novelty':novelty})

def novelty_new(request):
    if request.method == "POST":
        form = NoveltyForm(request.POST)
        if form.is_valid():
            novelty = form.save(commit=False)
            novelty.published_date = timezone.now()
            novelty.save()
            return redirect('feed')
    else:
        form = NoveltyForm()
    return render(request, 'feed/edit.html', {'form':form})

def novelty_edit(request, pk):
    novelty = get_object_or_404(Novelty, pk=pk)
    if request.method == 'POST':
        form = NoveltyFormForEdit(request.POST, instance=novelty)
        if form.is_valid():
            novelty.save()
            return redirect('feed')
    else:
        form = NoveltyFormForEdit(instance=novelty)
    return render(request, 'feed/edit.html', {'form':form})
