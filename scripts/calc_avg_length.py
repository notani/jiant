#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Show document lengths

from csv import DictReader
from os import listdir
from os import path
import argparse
import logging
import numpy as np
import pandas as pd


def get_lengths(dir_input):
    lengths = []
    for filename in listdir(dir_input):
        path_input = path.join(dir_input, filename)
        sep = '\t' if path_input.endswith('.tsv') else ','
        with open(path_input) as f:
            header = f.readline().strip().split(sep)
            cols = [i for i, col in enumerate(header)
                    if col.startswith('sentence')]
            for line in f:
                row = line.strip().split(sep)
                for i in cols:
                    lengths.append(len(row[i].split(' ')))
    return np.array(lengths)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_input', help='path to input directory')
    args = parser.parse_args()
    lengths = get_lengths(args.dir_input)
    print(f'Text: {len(lengths)}')
    print(f'Max: {lengths.max()}, Min: {lengths.min()}')
    print(f'Mean: {lengths.mean()}, Std: {lengths.std()}')
    percentiles = np.percentile(lengths, [25, 50, 75])
    print(f'Percentile[25, 50, 75]: {percentiles}')
