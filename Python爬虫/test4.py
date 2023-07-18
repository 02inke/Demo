import requests
import json
if __name__ == '__main__':
    print("-------------豆瓣爬取--------------")
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
        }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    print(list_data)
    with open('movies.json','w',encoding='utf-8') as fp:
        json.dump(list_data,fp=fp,ensure_ascii=False)
        
    print("抓取完成")
