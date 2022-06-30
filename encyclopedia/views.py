import random
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2 
from importlib.metadata import entry_points
from importlib.resources import contents
from ssl import TLSVersion
from urllib.request import Request
from django.shortcuts import redirect, render
from . import util
from .forms import *


def index(request):
    q = request.GET.get('q')
    entries = util.list_entries()
    
    if q: 
        entries = [ e for e in entries if q.lower() in e.lower()]
    if q in entries:
        return redirect('encyclopedia/single_entry', q)

    return render(request, "encyclopedia/index.html", {
         "entries": entries
    })



def single_entry(request, title:str):
    content = markdown2.markdown(util.get_entry(title))
    return render(request,"encyclopedia/single_entry.html", {
        "title" : title,
        "content" : content
    })
   
def create_entry(request):
    form = EntryCreatForm()
    if request.method == 'POST':
        form = EntryCreatForm(request.POST)
        if form.is_valid():
          title = form.cleaned_data['title']
          if title in util.list_entries():
             return  render(request, 'encyclopedia/error.html', {
                 'title': f'The entry {title} already exists!'
             })
          content = form.cleaned_data['content']
 
          util.save_entry(title, content)
           
        return redirect('index')

    return  render(request, 'encyclopedia/create_entry.html', { 
       'form': form,
    })
     
def random_entry(request):
     entries = util.list_entries()
     random_choice = random.choice(entries)
     return redirect('single_entry', random_choice
   )

def edit_entry(request, title:str):
        
       content=util.get_entry(title)
       editform = EditEntry(initial={
        'entry_title' : title,
        'entry_content' : content})

       if request.method=='POST':

          form= EditEntry(request.POST)
          if form.is_valid():
               edit_title = form.cleaned_data['entry_title']
               edit_cont = form.cleaned_data['entry_content']
               util.save_entry(edit_title,edit_cont)
               return redirect('single_entry',edit_title)
          else:
            return render(request, 'encyclopedia/edit_entry.html', {'title': title, 'form':form})



       return render(request, 'encyclopedia/edit_entry.html', {'title': title, 'form': editform})