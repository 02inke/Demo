#破解百度翻译
import requests
import json
import time
print("---------百度翻译----------")
if __name__ == '__main__':
    post_url = "https://fanyi.baidu.com/sug"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    s = 'y';
    a = 0;
    while (s == 'y' or s == 'Y'):
        word = input("enter a word:")
        data = {
            'kw':word
            }
        response = requests.post(url=post_url,data=data,headers=headers)
        #获取响应数据，json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json())
        dic_obj = response.json()
        print(dic_obj['data'][0]['v'])
        print('\n')
        time.sleep(3)
        s = input('是否继续(y or n):')
        
