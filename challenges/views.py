from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

monthly_challenges = {
  "january": "Eat meat for entire month",
  "february": "Walk for at least 20 minutes every day!",
  "march": "Code Django every day!",
  "april": "Eat meat for entire month",
  "may": "Code Django every day!",
  "jun": "Walk for at least 20 minutes every day!",
  "july": "Code Django every day!",
  "august": "Eat meat for entire month",
  "september": "Walk for at least 20 minutes every day!",
  "october": "Code Django every day!",
  "november": "Eat meat for entire month",
  "december": "Walk for at least 20 minutes every day!",
}
# Create your views here.
# def january(request):
#   return HttpResponse("Eat meat for entire month")

# def february(request):
#   return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#   return HttpResponse("Code Django every day!")
def monthly_challenges_by_number(request, month):
  months =list(monthly_challenges.keys())
  if month > len(months):
    return HttpResponseNotFound("Invalid month")
  forward_month = months[month -1]
  return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
  except:
    return HttpResponseNotFound("This month is not supported!")
  return HttpResponse(challenge_text)