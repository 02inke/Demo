import asyncio
import time
async def request(url):
    print('正在下载,',url)
    await asyncio.sleep(2)
    print('下载完毕,',url)
start_time = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.bilibili.com'
    ]
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print('%f'%(end_time-start_time))
