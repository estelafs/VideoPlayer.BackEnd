from django.shortcuts import render, redirect
from .forms import NewUrlEntryForm, NewUrlBookmarkedForm
from .models import UrlEntry, UrlBookmarked

def history(request):
    entries = UrlEntry.objects.order_by('add_at')
    context = {'entriesHistory': entries}
    return render(request, 'index.html', context)

def bookMarks(request):
    entries = UrlBookmarked.objects.order_by('add_at')
    context = {'entriesBookmark': entries}
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

def addBookmark(request):
    if request.method == "POST":
        form = NewUrlBookmarkedForm(request.POST)
        
        if form.is_valid():
            new_entry = UrlBookmarked(url=request.POST['url'])
        
            new_entry.save()
            return redirect('bookMarks')
        
    else:
        form = NewUrlEntryForm()
    
    context = {'form': form}
    return render(request, 'addBookmark.html', context)