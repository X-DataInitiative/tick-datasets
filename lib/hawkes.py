import os
from collections import OrderedDict

import numpy as np

from lib.dataset_analysis import print_characteristics
import glob

# name, path, number of realization
hawkes_datasets = [
    ('Bund', '../hawkes/bund/bund_*.npz', 20)
]


def iterate_hawkes_dataset_path():
    for name, path, *args in hawkes_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        yield name, path


def iterate_hawkes_dataset():
    for name, path, n_realizations in hawkes_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        timestamps_list = []
        for filepath in glob.glob(path):
            timestamps = np.load(filepath)
            timestamps_list += [timestamps['arr_0']]
        yield name, timestamps_list, n_realizations


def hawkes_characteristics(timestamps_list):
    characteristics = OrderedDict()
    n_realizations = len(timestamps_list)
    characteristics['Number of realizations'] = n_realizations

    n_nodes = len(timestamps_list[0])
    n_jumps_per_node = np.zeros(n_nodes)
    for timestamps in timestamps_list:
        for i in range(n_nodes):
            n_jumps_per_node[i] += len(timestamps[i])
    n_jumps_per_node /= n_realizations
    for i in range(n_nodes):
        characteristics['Average number of ticks node %i' % i] = \
            n_jumps_per_node[i]

    return characteristics


def describe_hawkes_datasets():
    for name, timestamps_list, *args in iterate_hawkes_dataset():
        characteristics = hawkes_characteristics(timestamps_list)
        print('\n{:}'.format(name))
        print_characteristics(characteristics, html=False)
