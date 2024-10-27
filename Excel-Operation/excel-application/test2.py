import pyttsx3

# 初始化 TTS 引擎
engine = pyttsx3.init()

# 设置语速（可选）
engine.setProperty('rate', 150)  # 默认是 200

# 设置音量（可选）
engine.setProperty('volume', 1)  # 范围是 0.0 到 1.0

# 要朗读的文本
text = 'qualifications资格'+'\n'+'footwear鞋'

# 朗读文本
engine.say(text)

# 等待朗读完成
engine.runAndWait()
