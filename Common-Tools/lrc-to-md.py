import re
import os


def lrc_to_md(lrc_file, param1):
    """
    将 LRC 格式转换为 Markdown 格式，并保存在同目录下的同名 `.md` 文件中。

    参数:
    - lrc_file: 输入的 LRC 文件路径
    - param1: 参数1，用于格式化输出
    """
    # 获取输出文件路径，替换扩展名为 .md
    md_file_path = os.path.splitext(lrc_file)[0] + '.md'

    try:
        with open(lrc_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"错误：找不到文件 {lrc_file}")
        return

    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        content_found = False  # 标记是否找到有效内容

        for line in lines:
            # 匹配时间戳格式 [mm:ss.xx]
            match = re.match(r'\[(\d{2}):(\d{2})\.(\d{3})\](.*)', line)
            if match:
                content_found = True  # 发现有效内容
                minutes = match.group(1)
                seconds = match.group(2)
                milliseconds = match.group(3)
                lyric_text = match.group(4).strip()

                # 将时间戳格式化为 "mm:ss.xx"
                timestamp = f"{minutes}:{seconds}.{milliseconds}"

                # 写入 Markdown 格式内容
                md_file.write(f"###### [[{param1}#t={timestamp}|{timestamp}]]\n")
                md_file.write(f"{lyric_text}\n")
            else:
                # 输出未匹配行信息以便调试
                print(f"未匹配行：{line.strip()}")

        if not content_found:
            print("警告：未找到有效的歌词内容，生成的文件可能为空。")

    print(f"转换完成，Markdown 文件已保存为 {md_file_path}")


# 示例用法
# lrc_file = input("请输入 LRC 文件路径：")  # 让用户输入 LRC 文件的路径
# param1 = input("请输入参数1：")  # 让用户输入参数1

lrc_to_md("C:\\Users\\admin\\Downloads\\Emerald Eyes-Anson Seabra.lrc", "Emerald Eyes-Anson Seabra.mp3")
