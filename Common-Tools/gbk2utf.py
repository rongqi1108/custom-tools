import os
from chardet import detect


def convert_gbk_to_utf8(path):
    """智能处理文件和目录"""
    if os.path.isdir(path):
        # 递归处理目录
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith(('.c', '.h', '.cpp')):
                    process_file(os.path.join(root, file))
    else:
        process_file(path)


def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            result = detect(content)

        if result['encoding'].lower() not in ['gbk', 'gb2312']:
            print(f"跳过非GBK文件: {file_path}")
            return

        # 创建备份
        # backup_path = file_path + '.gbk_bak'
        # os.rename(file_path, backup_path)
        # print(f"创建备份: {backup_path}")

        # 写入转换内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.decode('gbk'))
        print(f"转换成功: {file_path}")

    except PermissionError as e:
        print(f"权限不足: {file_path} | 错误: {e}")
    except Exception as e:
        print(f"处理失败: {file_path} | 错误: {e}")


if __name__ == "__main__":
    target_path = "F:\\projects\\eplayer\\EPlayerServer"  # 可以是文件或目录
    convert_gbk_to_utf8(target_path)