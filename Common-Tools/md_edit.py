# 读取 Markdown 文件
with open("input.md", "r", encoding="utf-8") as f:
    content = f.read()

# 条件修改示例：替换所有旧链接
new_content = content.replace("http://old-domain.com", "https://new-domain.com")

# 写入修改后的内容
with open("output.md", "w", encoding="utf-8") as f:
    f.write(new_content)