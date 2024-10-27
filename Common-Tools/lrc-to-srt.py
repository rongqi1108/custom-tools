import re
import os
from datetime import timedelta


def lrc_to_srt(file_path, keep_lyrics=True):
    # 确认文件路径
    if not file_path.endswith('.lrc'):
        raise ValueError("请输入 .lrc 文件")

    # 解析文件路径与名称
    base_name = os.path.splitext(file_path)[0]
    srt_path = f"{base_name}.srt"

    # 正则表达式匹配时间标签
    time_pattern = re.compile(r'\[(\d+):(\d+\.\d+)\]')

    srt_entries = []
    entry_count = 1

    with open(file_path, 'r', encoding='utf-8') as lrc_file:
        for line in lrc_file:
            # 找到所有时间标签和歌词内容
            matches = time_pattern.findall(line)
            lyric_text = time_pattern.sub('', line).strip()

            for match in matches:
                minutes, seconds = match
                total_seconds = int(minutes) * 60 + float(seconds)
                start_time = timedelta(seconds=total_seconds)

                # 添加一秒的时间来设置结束时间
                end_time = start_time + timedelta(seconds=1)

                # 格式化时间戳
                start_str = str(start_time)[:-3].replace('.', ',')
                end_str = str(end_time)[:-3].replace('.', ',')

                # 构建srt条目
                srt_entry = f"{entry_count}\n{start_str} --> {end_str}\n"
                if keep_lyrics:
                    srt_entry += f"{lyric_text}\n"

                srt_entries.append(srt_entry)
                entry_count += 1

    # 写入 .srt 文件
    with open(srt_path, 'w', encoding='utf-8') as srt_file:
        srt_file.write('\n'.join(srt_entries))

    print(f"转换完成，SRT 文件保存在: {srt_path}")


# 示例调用
lrc_to_srt('C:\\Users\\admin\\Downloads\\Lesson 1 Budget Cuts.lrc', keep_lyrics=False)
