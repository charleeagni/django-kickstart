# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def exampleGet(request):
    """
    this is an example get request
    :return:
    """
    try:
        exapmple_post = request.GET["get_example"]
    except Exception as e:
        print("get_example not found")

    return HttpResponse("response")

@csrf_exempt
def examplePost(request):
    """
    this is an example post request
    :return:
    """
    try:
        exapmple_post = request.POST["post_example"]
    except Exception as e:
        print("post_example not found")
    return HttpResponse("POST response")