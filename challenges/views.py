from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def january(request):
  return HttpResponse("Eat meat for entire month")

def february(request):
  return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#   return HttpResponse("Code Django every day!")
def monthly_challenges_by_number(request, month):
  return HttpResponse(month)

def monthly_challenge(request, month):
  challenge_text = None
  if month == "january":
    challenge_text = "Eat meat for entire month"
  elif month == "february":
    challenge_text = "Walk for at least 20 minutes every day!"
  elif month == "march":
    challenge_text = "Code Django every day!"
  else:
    return HttpResponseNotFound("This month is not supported!")
  return HttpResponse(challenge_text)