#需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
#UA：User-Agent(请求载体的身份标识)
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份
#        标识为某一款浏览器，就说明该请求是一个正常的请求，但是，如果检测到请求
#        的载体身份标识不是基于某一款浏览器，则表示该请求为不正常的请求（爬虫）
#        则服务器端就很有可能拒绝该次请求。

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
if __name__ == "__main__":
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
        
        }
    url =  "https://www.sogou.com/web?"  #query=啊毛
    #处理url携带的参数：封装到字典中
    kw = input("enter a word:")
    param = {
        'query':kw
        }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page = response.text
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page)
    print("爬取成功")
    print("{}.html保存成功".format(kw))
   #print(kw+".html保存成功")
