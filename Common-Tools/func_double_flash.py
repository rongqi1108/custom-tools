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


# 示例用法
input_string = "path/to//file"
output_string = add_slash_after_single_slash(input_string)
print("Original:", input_string)
print("Modified:", output_string)