import requests
from bs4 import BeautifulSoup

# Lottery Number 
# url : https://www.taiwanlottery.com.tw/

url = 'https://www.taiwanlottery.com.tw/'


html = requests.get(url)
html.encoding = 'utf8'
    
sp = BeautifulSoup(html.text, 'lxml')
if html.status_code == requests.codes.ok:
    datas = sp.find('div', class_='contents_box02')
    title = datas.find('span', class_='font_black15').text
    print(title)
    nums = datas.find_all('div', class_='ball_tx ball_green')
    for i in range(6,12):
        print(nums[i].text, end=' | ')

