from asyncio.windows_events import NULL
from curses.ascii import HT
from urllib import response
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect, Http404
from django.template.loader import render_to_string

import challenges
style = """
text-align: center;
margin: auto;
color: green;
background: linear-gradient(60deg, tomato, aqua);
width: 300px;
height: 50px;
align-items: center;
border-radius: 15px;

"""
# Create your views here.
weekly_challenges_text = {
    "sunday":'today is sunday',
    "monday":'today is monday',
    "tusday": 'today is tusday',
    "wednesday":'today is wednesday',
    "thursday":'today is thursday',
    "friday":'today is friday',
    "saturday": None

}


def index(request):
    
    days = list(weekly_challenges_text.keys())

    return render(request, "challenges/index.html", {
        "days": days
    })

def weekly_challenges_number(request, day):
    days = list(weekly_challenges_text.keys())
    if day > len(days):
        return HttpResponseNotFound("Sorry!")
    redirect_day = days[day-1]
    return HttpResponseRedirect(redirect_day)


def weekly_challenges(request, day):
    try: 
        weekly_challenge = weekly_challenges_text[day]
        return render(request, "challenges/challenge.html", {
            'text': weekly_challenge,
            'day': day
        })
    except:
       raise Http404()
