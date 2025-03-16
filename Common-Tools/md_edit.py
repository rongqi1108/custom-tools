import re
import os
import func_double_flash

def process_markdown_file(input_path, output_path=None):
    # 如果没有提供输出路径，则使用输入路径作为输出路径
    if output_path is None:
        output_path = input_path

    # 打开输入文件并读取内容
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 对代码块进一步替换处理
    def _process_code_blocks(match):
        # 提取代码块内容（包括语言标识后的所有内容） 提取第二个()的内容
        code_content = match.group(2)

        # 删除无序列表项（匹配所有以 - 开头且后跟数字的行）
        code_content = re.sub(r'^\s*-\s*\d+\s*$', '', code_content, flags=re.MULTILINE)

        # 删除![]开头的
        code_content = re.sub(r'^!\[].*\n', '', code_content, flags=re.MULTILINE)

        # 删除多余空行（保留单个空行）
        code_content = re.sub(r'\n{2,}', '\n', code_content)



        # 返回处理后的代码块（添加 cpp 标识）
        return f'```cpp\n{code_content.strip()}\n```'

    # 使用正则表达式匹配并处理代码块
    processed_content = re.sub(
        r'^\s*?``(`.*?)\n([\s\S]*?)\n\s*?```$',  # 提取代码块
        _process_code_blocks,  # 替换函数
        content,  # 原始内容
        flags=re.MULTILINE  # 标志
    )

    # 写入处理后的内容到输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)


if __name__ == '__main__':
    input_file = r'C:\Users\admin\Desktop\未归类\【侯捷 C++】STL标准库和泛型编程 超详细-万字笔记总结-学习笔记_侯捷stl-CSDN博客.md'
    output_file = r'C:\Users\admin\Desktop\未归类\STL标准库和泛型编程.md'

    # 处理 Markdown 文件
    process_markdown_file(func_double_flash.double_slash(input_file), func_double_flash.double_slash(output_file))
    print(f'处理完成，输出文件：{output_file}')
