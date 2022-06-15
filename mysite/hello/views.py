from django.http import HttpResponse

# Create your views here

def helloview(request):
    visitor_num = request.session.get("visitor_num", 0) + 1
    request.session["visitor_num"] = visitor_num
    if visitor_num > 4:
        del(request.session["visitor_num"])
    resp = HttpResponse("view count=" + str(visitor_num))
    resp.set_cookie('dj4e_cookie', '7aef8f65', max_age=1000)
    return resp