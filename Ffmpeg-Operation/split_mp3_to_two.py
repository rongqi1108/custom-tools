from pydub import AudioSegment
import os

def split_audio_file(file_path):
    # 加载音频文件
    audio = AudioSegment.from_file(file_path)

    # 获取音频时长（毫秒）
    duration = len(audio)

    # 计算中间点
    middle_point = duration // 2

    # 分割音频
    part1 = audio[:middle_point]
    part2 = audio[middle_point:]

    # 获取原文件名和目录
    base_name, ext = os.path.splitext(file_path)
    dir_name = os.path.dirname(file_path)

    # 新文件名
    part1_path = os.path.join(dir_name, f"{base_name}_part1{ext}")
    part2_path = os.path.join(dir_name, f"{base_name}_part2{ext}")

    # 导出音频文件
    part1.export(part1_path, format="mp3")
    part2.export(part2_path, format="mp3")

    print(f"音频已分割为:\n{part1_path}\n{part2_path}")

# 使用示例
split_audio_file("C:\\Users\\admin\\Downloads\\大脑想要这样学.mp3")
