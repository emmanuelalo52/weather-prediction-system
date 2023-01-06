import time
from bs4 import BeautifulSoup
import requests
from csv import writer
#requests information from a specified website
def find_weather():
    html_text = requests.get('https://weather.com/en-NG/weather/tenday/l/b8543529c433dce3265b04f5b9bbfd9776b4e4b61402261ae46ec2766ec23db9#detailIndex5').text
    soup = BeautifulSoup(html_text, 'html.parser')
    weathers = soup.find_all('div', class_ = 'DaypartDetails--Content--2Yg3_ DaypartDetails--contentGrid--2_szQ')
    with open('weather.csv','w',encoding='utf8',newline='') as f:
        thewriter = writer(f)
        header = ['Date','Temperature','Humidity']
        thewriter.writerow(header)
        for weather in weathers:
            date =  weather.find('span', class_ = 'DailyContent--daypartDate--3VGlz').text.replace('\n','')
            temperature = weather.find('span', class_ = 'DailyContent--temp--1s3a7').text.replace('\n','')
            humidity = weather.find('span', class_ = 'DetailsTable--value--2YD0-').text.replace('\n','')
            info = [date,temperature,humidity]
            thewriter.writerow(info)
find_weather()