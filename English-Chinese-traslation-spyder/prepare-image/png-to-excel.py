from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image as PILImage

# 加载现有的Excel文件
wb = load_workbook("output.xlsx")
sheet = wb.active

# 加载图片并调整大小
img = PILImage.open("D:\\图片\\shoplifter\\0.jpg")
img = img.resize((200, 200))  # 调整图片大小

# 将图片保存为临时文件
img_path = "temp_image.png"
img.save(img_path)

# 创建Excel图片对象
xl_img = XLImage(img_path)

# 设置图片位置
sheet.add_image(xl_img, 'C5')

# 保存更改
wb.save("output.xlsx")