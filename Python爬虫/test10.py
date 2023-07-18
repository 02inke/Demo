import requests
from lxml import etree
if __name__ == '__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
        }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    fp = open('./city.txt','w',encoding='utf-8')
    #热门城市
    hot_city_list = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
    fp.write('热门城市：\n')
    for i in hot_city_list:
        fp.write(i+'\t')
    fp.write('\n所有城市:\n')
    #所有城市
    all_city_list = tree.xpath('//div[@class="all"]/div[2]/ul')
    #循环每个首字母的所有城市
    for l_city in all_city_list:
        letter = l_city.xpath('./div/b/text()')[0]
        city = l_city.xpath('./div[2]/li/a/text()')
        temp = 0
        for a in city:
            if temp == 0:
                fp.write('\n'+letter+'\n')
            fp.write(a+'\t')
            temp = 1
    fp.close()
    print('保存完毕')
