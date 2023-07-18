#需求：爬取三国演义中所有的章节标题和章节内容
from bs4 import BeautifulSoup
import os
import re
import requests
if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    url = 'http://www.gushicimingju.com/novel/sanguoyanyi/'
    if not os.path.exists('./三国演义'):
        os.mkdir('./三国演义')
    page_text = requests.get(url=url,headers=headers).text
    #实例化一个BeautifulSoup对象
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.main-content > ul > li')
    for li in li_list:
        title = li.a.string
        fileName = './三国演义/'+title[:5]+'.txt'
        detail_url = 'http://www.gushicimingju.com' + li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_="main-content gushi-info")
        content = div_tag.text
        with open(fileName,'w',encoding='utf-8') as fp:
            fp.write(content)
        print(fileName,'爬取完成')
