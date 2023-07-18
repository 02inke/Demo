import requests
from lxml import etree
import json
import random
import re
from multiprocessing.dummy import Pool
print('--------------------研究失败，拜拜了您呢-----------------')
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
url = 'https://www.pearvideo.com/category_5'
origin_url = 'https://www.pearvideo.com/videoStatus.jsp'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    new_url = li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    se = '.*?(\d{7})'
    print(new_url)
    id_ = re.findall(se,new_url)[0]
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
        'Referer':'https://www.pearvideo.com/'+new_url
        }
    param = {
        'contld':id_,
        }
    response = requests.get(url=origin_url,params=param,headers=headers)
    json_data = response.json()
    print(json_data['videoInfo']['video_image'])
    '''
    with open('a.txt','a+',encoding='utf-8')as fp:
        json.dump(json_data,fp=fp,ensure_ascii=False)
#https://www.pearvideo.com/videoStatus.jsp?contId=1736562&mrd=0.6943987297591727
    '''
def getData(url):
    print('就这')
pool = Pool(4)
pool.map(getData,[1,2,3,4,5])
