import os
import subprocess

def convert_mkv_to_mp4(folder_path):
    # 遍历指定文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith('.mkv'):
            mkv_path = os.path.join(folder_path, filename)
            mp4_path = os.path.join(folder_path, filename[:-4] + '.mp4')

            # 使用ffmpeg进行转换
            try:
                subprocess.run(['ffmpeg', '-i', mkv_path, mp4_path], check=True)
                print(f'Converted: {filename} to {filename[:-4]}.mp4')
            except subprocess.CalledProcessError as e:
                print(f'Error converting {filename}: {e}')

# 示例用法
folder_path = 'F:\\电视剧\\6-[J门飞鹰]【2017】'  # 替换为你的文件夹路径
convert_mkv_to_mp4(folder_path)
