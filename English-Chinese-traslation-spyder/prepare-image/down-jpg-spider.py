import requests
import os
from lxml import etree
import re
import socket
# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(10)


def biying_pic_url(num, keyword):
    """
    该函数用于获取必应图片搜索结果的图片链接

    参数：
    num - 要获取的图片数量
    keyword - 搜索的关键词

    返回：
    一个包含图片链接的列表
    """
    pic_url= []  # 用于存储图片链接的列表
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}  # 定义请求头
    for i in range((num // 35) + 1):  # 根据指定的图片数量计算需要请求的页数
        page_url = 'https://cn.bing.com/images/async?q={}&first={}&count=35&relo=4&relp=5&cw=1117&ch=689&scenario=ImageBasicHover&datsrc=N_I&layout=ColumnBased&mmasync=1&dgState=c*6_y*1582s1599s1589s1660s1720s1704_i*40_w*172&IG=B3C2B933EAED48A4A82330EC1E7A638B&SFX=2&iid=images.5659'.format(keyword, i*35)  # 构造每页的 URL
        print(page_url)  # 打印当前请求的 URL
        html = requests.get(page_url, headers=headers).text  # 发送请求获取页面内容
        html = etree.HTML(html)  # 将页面内容转换为 HTML 格式
        conda_list = html.xpath('//a[@class="iusc"]/@m')  # 使用 XPath 提取特定属性的值
        for j in conda_list:  # 遍历提取到的属性值
            img_url = re.search('"murl":"(.*?)"', j).group(1)  # 使用正则表达式提取图片链接
            pic_url.append(img_url)  # 将图片链接添加到列表中
            if len(pic_url) == num :
                break
    return pic_url  # 返回图片链接列表

def down_img(num, keyword):
    """
    该函数用于下载图片

    参数：
    num - 要下载的图片数量
    keyword - 搜索的关键词，用于创建保存图片的文件夹
    """
    pic_url  = biying_pic_url(num, keyword)  # 获取图片链接

    if os.path.exists('D:/图片/'+keyword):  # 检查保存图片的文件夹是否存在
        pass
    else:
        os.makedirs('D:/图片/'+keyword)  # 如果不存在则创建

    path = 'D:/图片/'  # 定义图片保存的路径
    for index,i in enumerate(pic_url):  # 遍历图片链接
        try:
            filename = path + keyword + '/' + str(index) + '.jpg'  # 构造图片保存的文件名
            print(filename)  # 打印文件名
            with open(filename, 'wb+') as f:  # 以二进制写入模式打开文件
                f.write(requests.get(i).content)  # 写入图片内容
        except:
            continue  # 如果下载过程中出现异常则跳过

if __name__ == '__main__':
    keyword = 'dog'  # 定义搜索关键词
    num = int(input('请输入爬取图片数目：'))  # 接收用户输入的图片数量
    down_img(num, keyword)  # 调用函数下载图片