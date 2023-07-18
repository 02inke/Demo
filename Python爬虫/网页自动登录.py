from selenium import webdriver
from lxml import etree
import time
bro = webdriver.Edge(executable_path='C:\Python\msedgedriver.exe')
bro.get('https://www.taobao.com/')
#标签定位
search_input = bro.find_elements_by_id('q')
#标签交互
search_input[0].send_keys('Iphone')
#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
#点击搜索按钮
btn = bro.find_elements_by_css_selector('.btn-search')
btn[0].click()

bro.get('https://www.baidu.com')
time.sleep(2)
#回退
bro.back()
time.sleep(2)
bro.forward()

time.sleep(5)
bro.quit()
 
