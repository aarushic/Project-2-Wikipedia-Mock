from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from . import util

import markdown2
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entryname):
    if request.method == "GET":


        getentry = util.get_entry(entryname)
        try:
            return render(request, "encyclopedia/title.html", {
                "entryname": markdown2.markdown(getentry), "title": entryname
            })
        except:
            return render(request, "encyclopedia/title.html", {
                "entryname": "ERROR: The requested page was not found.", "title": "No title"
            })
    else:

        try:
            getentry = util.get_entry(request.POST['q'])
            return render(request, "encyclopedia/title.html", {
                "entryname" : markdown2.markdown(getentry), "title": entryname
            })
        except:
            getentry = request.POST['q']
            list=[]
            entries = util.list_entries()
            for entry in entries:
               if getentry in entry:
                    list.append(entry)
                    continue

            return render(request, "encyclopedia/index.html", {
                "entries": list
             })

def edit(request, name):
    getname = name
    if request.method == "GET":


        getentry = util.get_entry(name)
        try:
            return render(request, "encyclopedia/edit.html", {
                "info": getentry, "title":name
            })
        except:
            return render(request, "encyclopedia/title.html", {
                "entryname": "ERROR: The requested page was not found.", "title": "title"
            })


    else:
        change = request.POST['change']

        util.save_entry(getname, change)

        getentry = util.get_entry(name)


        return redirect('entry', entryname=getname)




def create(request):
    if request.method=="GET":
        return render(request, "encyclopedia/create.html")
    else:

        title = request.POST['title']
        info = request.POST['info']
        getentry = util.get_entry(title)

        if getentry is None:

            util.save_entry(title, info)
            getentry = util.get_entry(title)

            return redirect('entry', entryname=title)
        else:
            return render(request, "encyclopedia/title.html", {
                "entryname": "This page already exists.", "title": "title"
            })



def choose(request):
    entries = [entry for entry in util.list_entries()]
    re = random.choice(entries)
    getentry = util.get_entry(re)
    return render(request, "encyclopedia/title.html", {
        "entryname": markdown2.markdown(getentry), "title": re
    })

def watchlist(request, item):
        return render(request, "auctions/index.html")
