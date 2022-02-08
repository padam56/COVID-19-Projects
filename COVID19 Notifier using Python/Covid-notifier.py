# -*- coding: utf-8 -*-
import requests
import json
import plyer
import datetime
import time
while(1):
    r = requests.get("https://corona-rest-api.herokuapp.com/Api/Nepal/")
    print(type(r))
    news = r.text
    #print(news)

    dict1 = json.loads(news)
    newsdict = dict1["Success"]
    print(newsdict)
    #print("Today's cases: "+str(newsdict['todayCases']))
    
    tod = datetime.date.today()
    todstr = tod.strftime(" - %d/%m/20%y")
    plyer.notification.notify(
        title = "Covid-19 Notification"+todstr,
        message = "Total Cases: "+str(newsdict['cases'])+
        "\nTotal Deaths: "+str(newsdict["deaths"])+
        "\nToday's Cases: "+str(newsdict["todayCases"])+
        "\nToday's Deaths: "+str(newsdict["todayCases"]),
        app_icon = r"D:\Covid Notifier\icon.ico",
        timeout = 3
        )
    time.sleep(12*60*60)

# For continuous background running(cmd):
# pythonw.exe .\Covid-notifier.py