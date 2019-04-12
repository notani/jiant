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

from calc_avg_length import get_lengths

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_input', help='path to input directory')
    args = parser.parse_args()

    dirnames = []
    for segm in listdir(args.dir_input):
        if segm == 'spm':
            for vocabsize in [8000, 16000, 32000]:
                dirname = path.join(args.dir_input, segm, str(vocabsize))
                dirnames.append((f'spm-{vocabsize}', dirname))
            continue
        dirname = path.join(args.dir_input, segm)
        dirnames.append((segm, dirname))

    print('|'.join(['Name', 'Text', 'Mean', 'Std', 'Min',
                    '25%', '50%', '75%', 'Max']))
    print('|'.join(['-'] * 9))
    for name, d in dirnames:
        lengths = get_lengths(d)
        buff = [name, len(lengths),
                lengths.mean(), lengths.std(),
                lengths.min()]
        buff += list(np.percentile(lengths, [25, 50, 75]))
        buff += [lengths.max()]
        print('|'.join(str(v) for v in buff))
