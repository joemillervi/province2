import redis
import urllib2
import requests

def _getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    return response

def _setVariable(variable_name, variable_value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(variable_name, variable_value)

def get_city_info(city):
    r = requests.get('http://127.0.0.1:3000/city/{city}'.format(city=city))
    return r.content
#    return urllib2.urlopen('http://127.0.0.1:3000/{city}'.format(city=city)).read()
