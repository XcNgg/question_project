# encoding: utf-8
from flask import Flask,make_response
from io import BytesIO
app = Flask(__name__)

import random
from PIL import Image, ImageDraw, ImageFont

def get_image():
    '''
    返回图片验证码信息
    :return:
    '''
    width, height, font_size, font_num = 300, 100, 48, 5
    # bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # 背景颜色
    bg_color = (255,222,173)
    image = Image.new(mode='RGB', size=(width, height), color=bg_color) # 画布
    draw = ImageDraw.Draw(image, mode='RGB')     # 绘图类
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", font_size)  # 字体
    verify = str()
    for i in range(font_num):
        x = random.randint(i * (width / font_num), (i + 1) * (width / font_num) - font_size)
        y = random.randint(0, height - font_size)
        char = random.choice([chr(alpha) for alpha in range(65, 91)] + [str(num) for num in range(10)]) # 随机参数拼接给verify
        verify += char
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text((x, y), char, fill=color, font=font)

    by = BytesIO()
    # image.show()
    image.save(by,format='PNG')
    image_byte = by.getvalue()
    # 文字  和  字节  图片得信息
    return verify,image_byte


get_image()
# # 注册路由
# @app.route('/')
# def index():
#     '''
#     给用户做调用 展示对应的信息
#     :return:
#     '''
#     text,img  = get_image()
#     resp= make_response(img)
#     # 设置网页格式
#     resp.content_type = 'image/png'
#
#     return resp
#
# if __name__ == '__main__':
#     # 启动
#     app.run()


