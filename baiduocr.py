#!/usr/bin/env python
# encoding: utf-8

"""
@description: 百度ocr

@author: baoqiang
@time: 2019/3/14 下午10:31
"""

from aip import AipOcr
import os
import base64

config = {
    'appId': '15760442',
    'apiKey': 'wii1Nkc6xMzqLGt6UtMLEQ4b',
    'secretKey': '4Gl2Ijbf6WdEPnpjQqyFOBkf9BIY4P9N'
}

client = AipOcr(**config)

filepath = '/Users/baoqiang/Downloads/abc'


def process_path():
    for filename in os.listdir(filepath):
        if 'DS_Store' in filename:
            continue

        fullname = os.path.join(filepath, filename)

        text = img_to_str(fullname)

        print('{}\n{}'.format(fullname, '#' * 5))
        print(text)

        print('{}\n'.format('*' * 30))

        # break


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
    # b64image = base64.b64encode(image)
    result = client.basicGeneral(image)
    if 'error_code' in result and result['error_code'] != 0:
        print('err: {}, {}'.format(result['error_code'],result['error_msg']))
        return None

    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    # process_sample()
    process_path()
