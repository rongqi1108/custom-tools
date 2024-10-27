import pyttsx3
import re

DESK_PATH = 'C:\\Users\\admin\\Desktop\\'


def split_en_ch(mixed_list, english_list, chinese_list):
    for item in mixed_list:
        match = re.search(r'([a-zA-Z0-9\s.]+)([\u4e00-\u9fff]+.*)', item)
        if match:
            english_part = match.group(1)
            chinese_part = match.group(2)
        else:
            print('No match found')
        # 添加到相应的列表
        english_list.append(english_part)
        chinese_list.append(chinese_part)


def generate_txt_file(content, file_path):
    """
    生成一个TXT文件并写入内容。

    参数:
    content (str): 要写入文件的字符串内容。
    file_path (str): 文件的完整路径，包括文件名和扩展名。
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"文件已成功生成：{file_path}")
    except Exception as e:
        print(f"生成文件时出错：{e}")


def read_txt(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def tts(text):
    # 初始化 TTS 引擎
    engine = pyttsx3.init()

    # 设置语速（可选）
    engine.setProperty('rate', 140)  # 默认是 200

    # 设置音量（可选）
    engine.setProperty('volume', 1)  # 范围是 0.0 到 1.0

    # 朗读文本
    engine.say(text)

    # 等待朗读完成
    engine.runAndWait()
