from django.http.request import HttpRequest
from django.http.response import (Http404, HttpResponseNotFound,
                                  HttpResponseRedirect)
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

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
    "november": "Doing Great",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months_name": months})


def monthly_challenge_by_number(request, month):
    if month <= len(monthly_challenges):
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse(monthly_challenge, args=[redirect_month])  # will give the path eg /challenges/january
        return HttpResponseRedirect(redirect_path)
    else:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def monthly_challenge(request, month):
    try:
        month_challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": month_challenge, "month_name": month.capitalize()})
    except Exception:
        raise Http404()
