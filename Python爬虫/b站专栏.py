import requests
from bs4 import BeautifulSoup
import os
if not os.path.exists('./租房经验'):
    os.mkdir('./租房经验')
headers={
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
url = 'https://www.bilibili.com/read/cv12804436'
page_text = requests.get(url=url,headers=headers).text
#实例化一个BeautifulSoup对象
soup = BeautifulSoup(page_text,'lxml')
all_p = soup.find('div',class_='normal-article-holder read-article-holder')
title = './租房经验/' + soup.find('h1',class_='title').text + '.txt'
data = all_p.text
with open (title,'a+',encoding='utf-8')as fp:
    fp.write(data)
print('下载完成')

