#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Show document lengths

from os import listdir
from os import path
import argparse
import logging
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('dir_input', help='path to input directory')
args = parser.parse_args()

lengths = []
for filename in listdir(args.dir_input):
    path_input = path.join(args.dir_input, filename)
    print(f'Read {path_input}')
    sep = '\t' if path_input.endswith('.tsv') else ','
    df = pd.read_csv(path_input, sep=sep)
    for col in df.columns:
        if not col.startswith('sentence'):
            continue
        lengths += [len(s.split()) for s in df[col].values]

lengths = np.array(lengths)
print(f'Text: {len(lengths)}')
print(f'Max: {lengths.max()}, Min: {lengths.min()}')
print(f'Mean: {lengths.mean()}, Std: {lengths.std()}')
percentiles = np.percentile(lengths, [25, 50, 75])
print(f'Percentile[25, 50, 75]: {percentiles}')
