from bs4 import BeautifulSoup
from func_double_flash import double_slash
import urllib.request
import os

def download_file(url, save_path, filename):
    try:
        urllib.request.urlretrieve(url, save_path)
        return True
    except Exception as e:
        print(f"下载{filename}失败,{e}")
        return False

def download_audio(file_path, target_path):
    #file_path = 'F:\\cpp\\面试音频\\312.html'
    print(f"当前正在处理{file_path}")
    file_path = double_slash(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取数据
    data = []
    current_description = None

    for element in soup.find_all('div'):
        if 'ant-card-meta-description' in element.get('class', []):
            # 遇到新的描述，更新当前描述
            current_description = element.get_text(strip=True)
        elif 'Dynamic_userName__hIs+a' in element.get('class', []):
            # 提取用户名
            username = element.get_text(strip=True)
        elif 'FeaturedList_featuredReason__Db8iy' in element.get('class', []):
            # 提取特点
            feature = element.get_text(strip=True)
        elif 'AudioItem_audio__6DjxN' in element.get('class', []):
            # 提取音频 URL
            audio_tag = element.find('audio')
            if audio_tag and 'src' in audio_tag.attrs:
                audio_url = audio_tag['src']
            else:
                #print(f"警告: 未找到 <audio> 标签的 src 属性，跳过该记录。HTML 内容: {element.prettify()}")
                print(f"未找到{current_description}-{username}-{feature}的URL")
                continue  # 跳过该记录

            # 将当前描述、用户名、特点和音频 URL 组合为一条记录
            if current_description:
                data.append([current_description, username, feature, audio_url])

    # 保存到 CSV 文件
    # with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(['Description', 'Username', 'Feature', 'Audio URL'])  # 写入表头
    #     writer.writerows(data)  # 写入数据

    # print("数据已保存到 output.csv")

    # 遍历 data 中的每个元素
    for record in data:
        #print(f"记录: {record}")
        #如果需要访问记录中的每个字段，可以进一步遍历
        for i in range(len(record)):
            #print(f"字段 {i}: {record[i]}")
            filename = record[0] + '-' + record[1] + '-' + record[2]
            url = record[3]
            file_path = target_path +'\\' + filename + '.webm'
            file_path = file_path.replace('/', ' ')
            #print(f'filename={filename}')
            #print(f'file_path={file_path}')
            download_file(url, file_path, filename)
    #print("全部完成")

if __name__ == "__main__":
    target_path = 'F:\\cpp\\面试音频'
    # 遍历路径下的所有 .html 文件
    # for root, dirs, files in os.walk(target_path):
    #     for file in files:
    #         if file.endswith(".html"):
    #             file_path = os.path.join(root, file)
    #             #print(f"找到 HTML 文件: {file_path}")
    #             download_audio(file_path, target_path)

    download_audio("F:\\cpp\\面试音频\\310.html", target_path)
    download_audio("F:\\cpp\\面试音频\\311.html", target_path)
    download_audio("F:\\cpp\\面试音频\\312.html", target_path)
    download_audio("F:\\cpp\\面试音频\\319.html", target_path)





'''需要提取的关键内容
<div class="ant-card-meta-description">介绍一下TCP/IP模型和OSI模型的区别</div>
<div class="Dynamic_userName__hIs+a">C++-算法猫-学生 大三</div>
<div class="FeaturedList_featuredReason__Db8iy">表达清晰</div>
<div class="AudioItem_audio__6DjxN"><audio type="audio/mpeg" src="http://cdn.kamacoder.com/668d16261b009-668d16261a8d1.webm"></audio>

<div class="Dynamic_userName__hIs+a">C++-算法猫-学生 大三2</div>
<div class="FeaturedList_featuredReason__Db8iy">表达清晰2</div>
<div class="AudioItem_audio__6DjxN"><audio type="audio/mpeg" src="http://cdn.kamacoder.com/668d16261b009-668d16261a8d12.webm"></audio>

<div class="ant-card-meta-description">介绍一下TCP/IP模型和OSI模型的区别2</div>
...
文件夹                              username           feature      url
介绍一下TCP/IP模型和OSI模型的区别 C++-算法猫-学生 大三 表达清晰 http:xxx.webm  username.webm

'''