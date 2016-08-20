from django.http import HttpResponse

def render(request, city_info):
    html = '{response}'.format(response=city_info)
    return HttpResponse(html)
