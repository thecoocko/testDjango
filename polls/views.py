from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Hello
from django.template import context, loader
def index(req):
    latest_greetings_list = Hello.objects.order_by('id')[:2]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_greetings_list' : latest_greetings_list
    }
    return render(req,'polls/index.html',context)
    
def detail(req, hello_id):
    hello = get_object_or_404(Hello,pk=hello_id)
    return render(req,'polls/detail.html',{'question':hello})
def results(res, hello_id):
    res = "You're looking at the results of greeting %s."
    return HttpResponse(res % hello_id)

def index(req):
    latest_greetings_list = Hello.objects.order_by('id')[:2]
    output = ', '.join([h.greeting for h in latest_greetings_list])
    return HttpResponse(output)

# Create your views here.

