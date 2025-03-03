import re
import requests
import json
from contextlib import closing
import pprint
from tkinter import *
from mkdir import *

url = "https://www.bilibili.com/video/BV1Yv411Y7dd"

header = {
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
'Referer': 'https://www.bilibili.com'
}
s = requests.session()
video_id = re.findall("[\w.]*[\w:\-\+\%]",url)[3]
vid = json.loads(s.get('https://api.bilibili.com/x/web-interface/view?bvid='+video_id,headers=header).text)
ep = vid['data']['ugc_season']['sections'][0]['episodes']

ob_path = 'D:/projects/obsidian/我的同步空间/my-obsidian/4 项目/【英语学习】' # obsidian存放文件夹地址
folderName = 'Extra English'
all_path = '{}/{}'.format(ob_path, folderName)
note_path = '{}/{}'.format(all_path, '笔记')
mkdir(all_path)
mkdir(note_path)

for i in ep:
	title = i['title']
	bvid = i['bvid']
	video_url = 'https://www.bilibili.com/video/{}'.format(bvid)
	with open('{}/{}.md'.format(note_path, title), 'w', encoding="utf-8") as f:
		f.write('# 学习视频\n')
		line = '[{}]({})\n'.format(title, video_url)
		f.write(line)
		f.write('# 笔记\n')


with open('{}/学习清单.md'.format(all_path), 'a', encoding="utf-8") as f:
	f.write('# 学习清单\n')
	for i in ep:
		f.write('- [ ] [[{}]]\n'.format(i['title']))



