import os
import subprocess

def convert_flv_to_mp3(file_path):
    if file_path.endswith('.flv'):
        mp3_path = file_path[:-4] + '.mp3'  # 创建MP3文件名

        # 使用ffmpeg进行转换
        try:
            subprocess.run(['ffmpeg', '-i', file_path, mp3_path], check=True)
            print(f'Converted: {file_path} to {mp3_path}')
        except subprocess.CalledProcessError as e:
            print(f'Error converting {file_path}: {e}')
    else:
        print("The file is not an FLV file.")

# 示例用法
file_path = 'F:\\英语学习\\【P1】经典反战歌曲《OneDay》愿世界和平！.flv'  # 替换为你的FLV文件路径
convert_flv_to_mp3(file_path)
