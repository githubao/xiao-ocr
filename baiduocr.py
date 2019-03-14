#!/usr/bin/env python
# encoding: utf-8

"""
@description: 百度ocr

@author: baoqiang
@time: 2019/3/14 下午10:31
"""

from aip import AipOcr

config = {
    'appId': '15760442',
    'apiKey': 'wii1Nkc6xMzqLGt6UtMLEQ4b',
    'secretKey': '***'
}

client = AipOcr(**config)


def process_sample():
    # fullname = '/Users/baoqiang/Downloads/3.png'
    fullname = '/Users/baoqiang/Downloads/技术发展/技术栈1/01-源码分析.jpeg'
    text = img_to_str(fullname)
    print(text)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    process_sample()
