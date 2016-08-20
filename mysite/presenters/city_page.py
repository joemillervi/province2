from mysite.views.city import render

def get_city_and_profession_info(request, profession='software developer', city_1='San Francisco, CA', city_2='Seattle, WA'):
    #call logic here
    #assemble view  

    return render(request, profession, city_1)
