from mysite.views.city import render
from mysite.logic.base import get_city_info

def get_city_and_profession_info(request, profession='software-developer', city_1='San-Francisco,-CA', city_2='Seattle,-WA'):
    #call logic here
    #assemble view  
    return render(request,  get_city_info(city_1))
