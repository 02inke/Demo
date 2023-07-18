from selenium import webdriver
import requests
import time
bro = webdriver.Chrome('C:\Python\chromedriver.exe')
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
ak = bro.find_element_by_class_name('login-hd-account')
ak.click()
bro.fullscreen_window()
time.sleep(3)
bro.save_screenshot('./aa.png')

code_img = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img.location #验证码的左上角的坐标
size = code_img.size#验证码对应的长和宽
