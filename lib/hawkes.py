import os
from collections import OrderedDict
import numpy as np

from lib.dataset_analysis import print_characteristics

# name, path, number of realization, number of nodes, end_time
hawkes_datasets = [
    ('Bund', '../hawkes/bund/bund.npz', 20, 4, 50400)
]


def iterate_hawkes_dataset_path():
    for name, path, *args in hawkes_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        yield name, path


def iterate_hawkes_dataset():
    for name, path, n_realizations, n_nodes, end_time in hawkes_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        timestamps_dict = np.load(path)
        yield name, timestamps_dict, n_realizations, n_nodes, end_time


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
    for name, timestamps_dict, *args in iterate_hawkes_dataset():
        timestamps_list = [timestamps_dict[key]
                           for key in timestamps_dict.keys()]
        characteristics = hawkes_characteristics(timestamps_list)
        print('\n{:}'.format(name))
        print_characteristics(characteristics, html=False)
