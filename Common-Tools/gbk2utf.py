import os
from chardet import detect


def convert_gbk_to_utf8(path):
    """智能处理文件和目录"""
    if os.path.isdir(path):
        # 递归处理目录
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(file_path)
    else:
        process_file(path)


def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            result = detect(content)

        # 如果无法检测到编码，跳过
        if result['encoding'] is None:
            print(f"无法检测文件编码，跳过: {file_path}")
            return

        # 如果文件不是 GBK 编码，跳过
        if result['encoding'].lower() not in ['gbk', 'gb2312']:
            print(f"跳过非GBK文件: {file_path}")
            return

        # 创建备份（可选）
        # backup_path = file_path + '.gbk_bak'
        # os.rename(file_path, backup_path)
        # print(f"创建备份: {backup_path}")

        # 处理内容
        decoded_content = content.decode('gbk')
        cleaned_content = decoded_content.replace('\r\n', '\n').replace('\r', '\n').rstrip('\r\n')

        # 写入转换内容
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(cleaned_content)
        print(f"转换成功: {file_path}")

    except PermissionError as e:
        print(f"权限不足: {file_path} | 错误: {e}")
    except Exception as e:
        print(f"处理失败: {file_path} | 错误: {e}")

def add_slash_after_single_slash(input_string):
    result = ""
    length = len(input_string)

    i = 0
    while i < length:
        result += input_string[i]
        if input_string[i] == '/' and i > 0 and input_string[i + 1] != '/' and input_string[i - 1] != '/':
            result += '/'
        i += 1

    return result

if __name__ == "__main__":
    target_path = input("gbk转utf8-输入需要转换的文件夹路径：")
    convert_gbk_to_utf8(add_slash_after_single_slash(target_path))
    input("")
# pyinstaller --onefile gbk2utf.py