from django.http import HttpResponse

def render(request, profession, city_1):
    html = "%s%s" % (city_1, profession)
    return HttpResponse(html)
