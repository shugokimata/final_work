from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World. let's start CPB!!これから頑張って行きましょう。またこれはgithubの実行テストです")