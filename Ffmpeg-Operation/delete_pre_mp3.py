from pydub import AudioSegment

def trim_mp3(file_path, seconds_to_trim):
    # 加载MP3文件
    audio = AudioSegment.from_file(file_path)

    # 计算需要保留的音频
    trimmed_audio = audio[seconds_to_trim * 1000:]  # 转换为毫秒

    # 保存替换原文件
    trimmed_audio.export(file_path, format="mp3")

# 示例用法
file_path = "F:\\英语学习\\03 初阶饮食_第03集：自测版纯净原声.mp3"  # 替换为你的文件路径
seconds_to_trim = 1  # 要删除的秒数
trim_mp3(file_path, seconds_to_trim)
