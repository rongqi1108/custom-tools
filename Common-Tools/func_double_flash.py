import re


def double_slash(path):
    # 替换单个反斜杠
    path = re.sub(r'([^\\])\\([^\\])', r'\1\\\\\2', path)
    # 替换单个斜杠
    path = re.sub(r'([^/])/([^/])', r'\1//\2', path)
    return path

    # result = ""
    # length = len(input_string)
    # ch = '/'
    # i = 0
    # while i < length:
    #     result += input_string[i]
    #     if input_string[i] == '/' and i > 0 and input_string[i + 1] != '/' and input_string[i - 1] != '/':
    #         result += '/'
    #     i += 1

    # return result

# # 示例用法
# input_string = r"path/to\file"
# output_string = double_slash(input_string)
# print("Original:", input_string)
# print("Modified:", output_string)
