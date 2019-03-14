#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用deep ocr

@author: baoqiang
@time: 2019/3/14 下午9:06
"""

import os

filepath = '/Users/baoqiang/Downloads/技术发展/技术栈1'

def process_path():
    for filename in os.listdir(filepath):
        fullname = os.path.join(filepath, filename)

        # process_image(fullname)

        break


if __name__ == '__main__':
    process_path()


