from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloview(request):
    visitor_num = request.session.get("visitor_num", 0) + 1
    request.session["visitor_num"] = visitor_num
    if visitor_num > 4:
        del(request.session["visitor_num"])
    response = HttpResponse("view count = " + str(visitor_num))
    return response