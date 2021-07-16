from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
monthly_challenges = {
    "january": "go for a walk atleast 20min",
    "february": "learn django",
    "march": "qwerty",
    "april": "suyash",
    "march": "mahajan",
    "may": "go for a walk atleast 20min",
    "june": "learn django",
    "july": "qwerty",
    "august": "suyash",
    "september": "mahajan",
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    if month == "january":
        return HttpResponse("jan")
    elif month == "february":
        return HttpResponse("feb")
    elif month == "march":
        return HttpResponse("march")
    elif month == "april":
        return HttpResponse("april")
    elif month == "may":
        return HttpResponse("may")
    elif month == "june":
        return HttpResponse("june")
    elif month == "july":
        return HttpResponse("july")
    elif month == "august":
        return HttpResponse("august")
    elif month == "september":
        return HttpResponse("sept")
    else:
        return HttpResponse(f"MonthError")
