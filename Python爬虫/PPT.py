import requests
from lxml import etree
import os
if __name__=='__main__':
    if not os.path.exists('./ppt模板'):
        os.mkdir('./ppt模板')
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
        }
    url = 'https://sc.chinaz.com/ppt/free.html'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    div = tree.xpath('//div[@class="container clearfix"]/div[4]/div')
    for s_div in div:
        html = 'https://sc.chinaz.com' + s_div.xpath('.//div[@class="bot-div"]/a/@href')[0]
        name = s_div.xpath('./div//img/@alt')[0]
        name = './ppt模板/' + name.encode('iso-8859-1').decode('utf-8') + '.rar'
        new_page_text = requests.get(url=html,headers=headers).text
        newTree = etree.HTML(new_page_text)
        a_url = newTree.xpath('//div[@class="container ppt-detail clearfix"]//div[@class="download-url"]/a/@href')[0]
        data = requests.get(url=a_url,headers=headers).content
        with open (name,'wb') as fp:
            fp.write(data)
        print(name,'下载完成!')
