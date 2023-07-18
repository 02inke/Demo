import requests
from lxml import etree
from chaojiying import Chaojiying_Client
print("-------------------模拟登录超级鹰---------------")
session = requests.Session()
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
url = 'http://www.chaojiying.com/user/login/'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_src = 'http://www.chaojiying.com' + tree.xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img/@src')[0]
imgData = session.get(url=code_src,headers=headers).content
with open('./code.jpg','wb')as fp:
    fp.write(imgData)
if __name__ == '__main__':
    chaojiying = Chaojiying_Client('3240175569', '3240175569', '920845')
    img = open('./code.jpg', 'rb').read()					    
    imgTxt = chaojiying.PostPic(img, 1004)['pic_str']
    url = 'http://www.chaojiying.com/user/login/'
    data = {
        'user':'3240175569',
        'pass':'3240175569' ,
        'imgtxt': imgTxt,
        'act': '1',
        }
    response = session.post(url=url,headers=headers,data=data)
    print(response)
    page_text = response.text
    with open('./c.html','w',encoding='utf-8')as fp:
        fp.write(page_text)
    print('保存完毕')
    


