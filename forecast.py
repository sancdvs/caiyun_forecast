import json
import re
import time
import requests
from data import data

skycon_zh = {'CLEAR_DAY':'晴','CLEAR_NIGHT':'晴','PARTLY_CLOUDY_DAY':'多云','PARTLY_CLOUDY_NIGHT':'多云','CLOUDY':'阴','LIGHT_HAZE':'轻度霾','MODERATE_HAZE':'中度霾','HEAVY_HAZE':'重度霾','LIGHT_RAIN':'小雨','MODERATE_RAIN':'中雨','HEAVY_RAIN':'大雨','STORM_RAIN':'暴雨','FOG':'雾','LIGHT_SNOW':'小雪','MODERATE_SNOW':'中雪','HEAVY_SNOW':'大雪','STORM_SNOW':'暴雪','DUST':'浮尘','SAND':'沙尘','WIND':'大风','THUNDER_SHOWER':'雷阵雨','HAIL':'冰雹','SLEET':'雨夹雪'}

def lal(city):
    for i in data:
        if i[2] and city in i[2]:
            return str(i[3])+','+str(i[4])
            
    for i in data:
        if i[1] and city in i[1]:
            return str(i[3])+','+str(i[4])

def forecast():
    city = input('输入地址：')
    url = 'http://api.caiyunapp.com/v2.5/TAkhjf8d1nlSlspN/%s/daily.json?dailysteps=15&hourlysteps=360'%(lal(city))

    content = requests.get(url).text
    content = json.loads(content)
    content = content['result']['daily']

    skycon = content['skycon']
    pressure = content['pressure']
    temperature = content['temperature']
    humidity = content['humidity']
    astro = content['astro']

    fx = []
    for i in range(len(skycon)):
        
        fx.append(skycon[i]['date'][:10]+'\t'+\
        
        skycon_zh[skycon[i]['value']]+'\t'+\

        re.findall(r'.*?\..',str(temperature[i]['min']))[0]+'-'+re.findall(r'.*?\..',str(temperature[i]['max']))[0]+' ℃'+'\t'+\

        str(int(humidity[i]['min']*100))+'-'+str(int(humidity[i]['max']*100))+' %RH'+'\t'+\

        re.findall(r'.*?\..',str(float(pressure[i]['avg'])/1000))[0]+' kPa'+'\t'+\

        astro[i]['sunrise']['time']+'-'+astro[i]['sunset']['time']+'\n')

    return fx


while True:
    for i in forecast():
        print(i)

