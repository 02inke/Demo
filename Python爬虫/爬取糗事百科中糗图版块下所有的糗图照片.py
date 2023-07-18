#爬取糗事百科中糗图版块下所有的糗图照片
import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    while True:
        pageNum = input('想爬取哪一页(输入q!退出)：')
        if pageNum=='q!':
            break
        if pageNum<'1'or pageNum>'14':
            print("非法输入")
            continue
        #设置一个通用的url模板
        url = 'https://www.qiushibaike.com/imgrank/page/'+pageNum
        #使用通用爬虫对一整张页面进行爬取
        page_text = requests.get(url=url,headers=headers).text

        #使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        for src in img_src_list:
            src = 'https:'+src
            img_name = src.split('/')[-1]
            imgPath = 'qiutuLibs/'+img_name
            img_data = requests.get(url=src,headers=headers).content
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
            print(img_name,'下载成功')
