# -*- coding：utf-8 -*-
import requests
import json
import os
import random
import socket
# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(10)

def baidu_pic_url(num, keyword):
    pic_url= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    for i in range((num // 30) + 1):

        page_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn={}&rn=30&gsm=1e&1581069586398='.format(keyword, keyword, 30*i)
        # print(page_url)
        r = requests.get(page_url, headers=headers).text
        res = json.loads(r)['data']
        if res:
            print(res)
            for j in res:
                try:
                    url = j['middleURL']
                    pic_url.append(url)
                    if len(pic_url) == num:
                        break
                except:
                    print('该图片的url不存在')

    print(len(pic_url))
    return pic_url

def down_img(num, keyword):
    pic_url  = baidu_pic_url(num, keyword)
    if os.path.exists('D:/图片/'+keyword):
        pass
    else:
        os.makedirs('D:/图片/'+keyword)

    path = 'D:/图片/'
    for index,i in enumerate(pic_url):
        try:
            filename = path + keyword + '/' + str(index) + '.jpg'
            print(filename)
            with open(filename, 'wb+') as f:
                f.write(requests.get(i).content)
        except:
            continue
if __name__ == '__main__':
    keyword = ''
    num = int(input('请输入爬取图片数目：'))
    down_img(num, keyword)

