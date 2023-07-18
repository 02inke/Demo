import requests
import os
import re
import aiohttp
import time
from lxml import etree
start_time = time.time()
if __name__ == "__main__":
    print('-------------------------------------------------最成功的龙骑士，只抓掉率最低的那条龙---------------------------------------------')
    if not os.path.exists('./妹子图'):
        os.mkdir('./妹子图')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
        }
    #解析初始页面
    a_list = ['fengjing','meinv','youxi','dongman','yingshi','mingxing','qiche','dongwu','rewu','meishi','zongjiao','beijing']
    print(a_list)
    ax = input('请选择下载的图片类型:')
    url = 'https://pic.netbian.com/4k'+ax+'/'#fengjing/meinv/youxi/dongman/yingshi/mingxing/qiche/dongwu/rewu/meishi/zongjiao/beijing
    #获取该页
    response = requests.get(url=url,headers=headers)
    page_text = response.content
    #获取总页数
    tree = etree.HTML(page_text)
    page = tree.xpath('//div[@class="page"]/a/text()')[-2]
    page = int (page)
    i = 1
    #循环每一页
    for p in range(1,page):
        if i==50:
            break
        init_url = 'https://pic.netbian.com/4k'+ax+'/index_%d.html'
        if p==1:
            url = 'https://pic.netbian.com/4k'+ax+'/'
        else:
            url = format(init_url%p)
        page_text = requests.get(url=url,headers=headers).text
        tree = etree.HTML(page_text)
        web_list = tree.xpath('//div[@class="slist"]/ul/li')
        #下载当页图片
        for web in web_list:
            new_url = 'https://pic.netbian.com' + web.xpath('./a/@href')[0]
            new_page_text = requests.get(url=new_url,headers=headers).text
            new_tree = etree.HTML(new_page_text)
            renew_url = 'https://pic.netbian.com'+new_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
            img_name = new_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0]
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_name = './妹子图/' + img_name + '.jpg'
            img_data = requests.get(url=renew_url,headers=headers).content
            with open(img_name,'wb') as fp:
                fp.write(img_data)
            print(img_name,'第%d张下载完成'%i)
            i+=1
            if i==50:
                break
end_time = time.time()
print('%d'%(end_time-start_time))

