# encoding:UTF-8
from bs4 import BeautifulSoup
import requests

def test():
    url = "http://liansai.500.com/"
    wb_data = requests.get(url, 'UTF-8')
    soup = BeautifulSoup(wb_data.text, 'lxml')
    
    f = open('./soup.txt', 'w', encoding='UTF-8')
    item = soup.select('.lhot_race_a')
    for i in item:
        f.write(str( i.get('href')))
    f.close
    
    
test()
