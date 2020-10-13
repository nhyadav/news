
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
import json
import datetime
import random
import itertools

def main(request):
    return HttpResponseRedirect('/news/')

class mainviews(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        if q:
            with open('data.json', 'r') as fout:
                data = json.load(fout)
            for dt in data:
                if q == dt['title']:
                    context = {'title': dt['title'], 'data': dt}
                    return render(request, 'search.html', context=context)
            return render(request, 'nosearch.html')

        else:
            date = []
            with open('data.json', 'r') as fo :
                data = json.load(fo)
            sotdata = sorted(data, key=lambda i : i['created'], reverse=True)
            sortdate = itertools.groupby(sotdata, lambda i : i['created'][:10])
            for k, v in sortdate :
                date.append(k)
            context = {'data': data, 'date': date}
            return render(request, 'index.html', context=context)


def abuot(request, p_sid):
    with open('data.json','r') as foo:
        dictdata = json.load(foo)
    home = ''
    for d in dictdata:
        if d["link"] == p_sid :
            home = f'<h2>{d["title"]}</h2><p>{d["created"]}</p>{d["text"]}<p>'

    return HttpResponse(home)

def login(request):
    return HttpResponse("<h2>this is a login  page </h2>")



class create(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')
    def post(self, request, *args, **kwargs):
        with open('data.json', 'r') as f :
            data = json.load(f)
        text = request.POST.get('text')
        title = request.POST.get('title')
        createdtime = datetime.datetime.now()
        created = datetime.datetime.strftime(createdtime, '%Y-%m-%d %H:%M:%S')
        link = random.randint(1, 10)
        stdata = {"created" : str(created), "text" : text, "title" : title, "link" : link}
        data.append(stdata)
        with open('data.json', 'w') as fout :
            json.dump(data, fout)
        return redirect('/')