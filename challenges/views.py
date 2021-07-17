from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.http.request import HttpRequest
from django.urls import reverse
from django.shortcuts import redirect, render

# Create your views here.
monthly_challenges = {
    "january": "go for walk atleast 20min",
    "february": "learn django for atleat 1 hour ",
    "march": "learn web development",
    "april": "Go for a drive",
    "may": "go for a walk atleast 20min",
    "june": "celebrate birthday",
    "july": "learn django",
    "august": "suyash",
    "september": "mahajan",
}


def monthly_challenge_by_number(request, month):
    if month <= len(monthly_challenges):
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path =  reverse(monthly_challenge, args=[redirect_month]) #will give the path eg /challenges/january
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invaid Month")


def monthly_challenge(request, month):
    try:
        return HttpResponse(f"<h1>{monthly_challenges[month]}</h1>")
    except KeyError:
        return HttpResponseNotFound("<h1>Month not found</h1>")

def months_list(request):
    list_item = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_link = reverse(monthly_challenge, args=[month])
        list_item += f'<li><a href="{month_link}">{month.capitalize()}</a></li>'
     
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)