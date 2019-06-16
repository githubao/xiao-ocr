#!/usr/bin/env python
# encoding: utf-8

"""
@description: 转化图片格式

@author: baoqiang
@time: 2019-03-31 23:58
"""

import os
from PIL import Image

inpath = '/Users/baoqiang/Downloads/app'
outpath = '/Users/baoqiang/Downloads/abc'


def convert():
    for filename in os.listdir(inpath):
        if 'DS_Store' in filename:
            continue

        convert_item(filename)

        # break


def convert_item(filename):
    fullname = os.path.join(inpath, filename)

    img = Image.open(fullname)

    outfile = os.path.join(outpath, filename.replace('.jpg', '.png'))

    img.save(outfile,format='png')


if __name__ == '__main__':
    convert()
