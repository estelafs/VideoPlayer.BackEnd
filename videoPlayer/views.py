from django.shortcuts import render, redirect
from .forms import NewUrlEntryForm
from .models import UrlEntry

def history(request):
    entries = UrlEntry.objects.order_by('add_at')
    context = {'entries': entries}
    return render(request, 'index.html', context)

def bookMarks(request):
    entries = UrlEntry.objects.order_by('add_at')
    context = {'entries': entries}
    return render(request, 'bookMarks.html', context)

def addEntry(request):
    if request.method == "POST":
        form = NewUrlEntryForm(request.POST)
        
        if form.is_valid():
            new_entry = UrlEntry(url=request.POST['url'])
        
            new_entry.save()
            return redirect('history')
        
    else:
        form = NewUrlEntryForm()
    
    context = {'form': form}
    return render(request, 'addEntry.html', context)