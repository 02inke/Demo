import requests
if __name__ == '__main__':
    print("kfc餐厅爬取")
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    param = {
        'op':'keyword',
        'cname':'',
        'pid':'',
        'keyword': '上海',
        'pageIndex': '1',
        'pageSize': '10',
        }
    response = requests.post(url=url,params=param,headers=headers)
    dic_data = response.text
    print(dic_data)
    with open('kfc餐厅.txt','w',encoding='utf-8') as fp:
        fp.write(dic_data)
