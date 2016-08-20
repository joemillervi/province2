from django.conf.urls import url
from mysite.presenters.city_page import get_city_and_profession_info

urlpatterns = [
    url(r'(?P<city_1>[A-Za-z0-9\-\_]+)/(?P<city_2>[0-9]{4})/(?P<profession>[0-9]{4})/$', get_city_and_profession_info),
  #  url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
  #  url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]
