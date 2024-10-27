import requests
import time
# -*- coding：utf-8 -*-
import requests
import json
import os
import random
import socket
# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(10)

def sougou_pic_url(num, keyword):
    pic_url= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    for i in range((num // 48) + 1):
        url = 'https://pic.sogou.com/pics?query=' + keyword + '&mode=1&start={}&reqType=ajax&reqFrom=result&tn=0'.format(i * 48)
        imgs = requests.get(url)
        jd = json.loads(imgs.text)
        jd = jd['items']
        for j in jd:
            pic_url.append(j['pic_url'])
            # if len(pic_url) == num:
            #     break
    print(len(pic_url))
    return pic_url

def down_img(num, keyword):
    pic_url  = sougou_pic_url(num, keyword)

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
    keyword = 'girl'
    num = int(input('请输入爬取图片数目：'))
    down_img(num, keyword)
