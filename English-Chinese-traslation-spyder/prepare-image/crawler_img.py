import os
import requests
from baidu_img import baidu_pic_url
from sougou_img import sougou_pic_url
from biying_img import biying_pic_url

class Crawler():
    def __init__(self, num, keyword, engine):
        self.num = num
        self.keyword = keyword
        self.engine = engine

    def down_img(self):
        if self.engine == 'baidu':
            pic_url = baidu_pic_url(self.num, self.keyword)
        elif self.engine == 'sougou':
            pic_url = sougou_pic_url(self.num, self.keyword)
        elif self.engine == 'biying':
            pic_url = biying_pic_url(self.num, self.keyword)
        else:
            print('错误的搜索引擎，请重新运行，输入：baidu、sougou、biying')

        if os.path.exists('D:/图片/' + self.engine + '/' + self.keyword):
            pass
        else:
            os.makedirs('D:/图片/' + self.engine + '/' + self.keyword)

        path = 'D:/图片/' + self.engine + '/'
        for index, i in enumerate(pic_url):
            try:
                filename = path + self.keyword + '/' + str(index) + '.jpg'
                print(filename)
                with open(filename, 'wb+') as f:
                    f.write(requests.get(i).content)
            except:
                continue

if __name__ == '__main__':
    keyword = str(input('请搜索关键词：（如：美女）'))
    num = int(input('请输入爬取图片数目：'))
    engine = str(input('请输入：baidu, sougou, biying其中之一'))
    crawler = Crawler(num, keyword, engine)
    crawler.down_img()

