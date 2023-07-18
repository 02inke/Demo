from selenium import webdriver
from lxml import etree
import time
bro = webdriver.Edge(executable_path='./msedgedriver.exe')
#让浏览器发起一个指定URL的请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#获取浏览器当前页面的源码数据
page_text = bro.page_source
#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
bro.quit()
