from selenium import webdriver
import time
print('---------------模拟登陆QQ空间---------------')

bro = webdriver.Edge('C:\Python\msedgedriver.exe')
bro.get('https://qzone.qq.com/')
print(bro.page_source)
bro.switch_to.frame('login_frame')
tag = bro.find_element_by_id('switcher_plogin')
tag.click()

user_name = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')

user_name.send_keys('3240175569')
time.sleep(1)
password.send_keys('12345678890')
time.sleep(1)

btn = bro.find_element_by_id('login_button')
btn.click()

time.sleep(5)
bro.quit()

