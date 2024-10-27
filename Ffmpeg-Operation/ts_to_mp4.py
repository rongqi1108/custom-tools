import os
import subprocess


def convert_ts_to_mp4(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.ts'):
            ts_path = os.path.join(folder_path, filename)
            mp4_filename = filename.replace('.ts', '.mp4')
            mp4_path = os.path.join(folder_path, mp4_filename)

            # 使用 ffmpeg 命令转换文件
            command = ['ffmpeg', '-i', ts_path, mp4_path]
            subprocess.run(command)
            print(f'Converted: {filename} to {mp4_filename}')


# 调用函数
convert_ts_to_mp4('你的文件夹路径')
