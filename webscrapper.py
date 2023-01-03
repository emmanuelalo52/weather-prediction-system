import time
from bs4 import BeautifulSoup
import requests
#requests information from a specified website
def find_weather():
    html_text = requests.get('https://www.timeanddate.com/weather/nigeria/lagos/ext').text
    soup = BeautifulSoup(html_text, 'html.parser')
    weathers = soup.find_all('table', class_ = 'zebra tb-wt fw va-m tb-hover sticky-en')
    for weather in weathers:
        date =  weather.find('th', class_ = 'smaller soft').text.replace(' ','')
        temperature = weather.find('span', class_ = 'sep').tbody.tr.th.text.replace(' ','')
        #humidity = weather.find('span', class_ = 'DetailsTable--value--2YD0').text.replace('\n','')
        #save as files
        with open(f'posts/{weather}.txt','w') as f:
            f.write(f"Date:{date.strip()}\n")#strip is to removed the irrelevant spacings
            f.write(f"Temperature:{temperature.strip()}\n")
            
            print(f'file saved:{weather}')
find_weather()