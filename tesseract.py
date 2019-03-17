#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文字识别

@author: baoqiang
@time: 2019/3/14 下午8:50
"""

import os
from PIL import Image
import pytesseract

filepath = '/Users/baoqiang/Downloads/技术发展/技术栈1'


def process_sample():
    # fullname = '/Users/baoqiang/Downloads/2.png'
    fullname = '/Users/baoqiang/Downloads/技术发展/技术栈2/02-数据结构和算法.jpeg'

    image = Image.open(fullname)

    text = pytesseract.image_to_string(image, lang='chi_sim', config='--psm 6')
    # text = pytesseract.image_to_string(image)

    print(text)


def process_path():
    for filename in os.listdir(filepath):
        fullname = os.path.join(filepath, filename)

        image = Image.open(fullname).convert('LA')

        text = pytesseract.image_to_string(image, lang='chi_sim')

        print(text)

        print('{}\n'.format('*' * 30))

        break


if __name__ == '__main__':
    process_sample()
    # process_path()
