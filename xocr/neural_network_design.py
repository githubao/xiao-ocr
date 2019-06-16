#!/usr/bin/env python
# encoding: utf-8

"""
@description: train & test

@author: baoqiang
@time: 2019-06-16 17:24
"""

import numpy as np
from sklearn.model_selection import train_test_split
import sys

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/baoqiang/xiao/python_repos/xiao-ocr'])

try:
    from xocr.ocr import OCRNeuralNetwork
except:
    pass


def valid(data_matrix, data_labels, test_indices, nn):
    avg_sum = 0
    for j in range(100):
        correct_guess_count = 0
        for i in test_indices:
            test = data_matrix[i]
            prediction = nn.predict(test)
            if data_labels[i] == prediction:
                correct_guess_count += 1

        avg_sum += correct_guess_count / float(len(test_indices))

    return avg_sum / 100


def run():
    data_matrix = np.loadtxt(open('data.csv', 'rb'), delimiter=',').tolist()
    data_labels = np.loadtxt(open('dataLabels.csv', 'rb')).tolist()

    train_indices, test_indices = train_test_split(list(range(5000)))

    print("PERFORMANCE")
    print("-" * 20)

    for i in range(5, 50, 5):
        nn = OCRNeuralNetwork(i, data_matrix, data_labels, train_indices, False)
        performance = valid(data_matrix, data_labels, test_indices, nn)

        print('{i} Hidden Nodes: {val:.4f}'.format(i=i, val=performance))
        sys.stdout.flush()

"""
5 Hidden Nodes: 0.7936
10 Hidden Nodes: 0.8496
15 Hidden Nodes: 0.8832
20 Hidden Nodes: 0.8864
25 Hidden Nodes: 0.8928
30 Hidden Nodes: 0.8936
35 Hidden Nodes: 0.8872
40 Hidden Nodes: 0.8984
45 Hidden Nodes: 0.8984
"""

if __name__ == '__main__':
    run()
