import requests
import json
import time
if __name__ == '__main__':
    print("----------药监局前50页数据的爬取-----------")
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []#存储企业的ID
    all_detail_data = []#存储所有的详情数据
    for page in range(1,51):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType':'1',
            'applyname':'', 
            'applysn':'' 
            }
        response = requests.post(url=url,data=data,headers=headers)
        dic_data = response.json()
        for item in dic_data['list']:
            id_list.append(item['ID'])
        print("第%s页抓取完成"%page)
        if int(page)%50==0:
            time.sleep(5)
    #获取企业详情数据
    a = 1
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
            }
        detail_data = requests.post(url=post_url,data=data,headers=headers).json()
        all_detail_data.append(detail_data)
        print("第%d家企业存储完成"%a)
        a += 1
    #持久化存储
    with open('allData.json','w',encoding='utf-8') as fp:
        json.dump(all_detail_data,fp=fp,ensure_ascii=False)
    print("存储完成")
        
