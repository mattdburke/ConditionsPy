#!/usr/bin/env python3

# ConditionsPy

# This program is designed to be deployed to a small Raspberry Pi model using CRON. This allows scheduling.

# Assign your email address to me
# Assign your password to password
# Assign the recipient email to you

me = '<Your email address here>' # Fill in string with email address
password = '<Password here>' # Fill in string with email password
you = '<Recepient address>' # Add recepient address

import requests
import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
from threading import Timer

# Get weather

def return_weather():
    # get peak district weather
    r = requests.get("https://www.mwis.org.uk/forecasts/english-and-welsh/peak-district/text")
    # apply soup DOM parsing
    soup = bs(r.text, "html.parser")
    # return weather for t+1
    forecast1 = soup.find("div", id="Forecast1")
    # extract all headers from table
    tags = forecast1.find_all("h4")
    weather_tags = forecast1.find_all("p")
    # define lists for reconstructing data
    weather_key = []
    weather_value = []
    # iterate and get text
    for i,v in zip(tags, weather_tags):
        weather_key.append(i.text)
        weather_value.append(v.text)
    weather_value = [i.replace('\n', ' ') for i in weather_value]
    text = ""
    for k, v in zip(weather_key, weather_value):
        text += "".join("%s \n %s \n" % (k, v))
    msg = EmailMessage()
    msg.set_content(text)
    msg['From'] = me
    msg['To'] = you
    msg['Subject'] = 'Peak District Weather for Tomorrow'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(me, password)
    s.send_message(msg)
    s.quit()

return_weather()
