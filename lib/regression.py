import os

import numpy as np
from sklearn.datasets import load_svmlight_file

from lib.dataset_analysis import features_characteristics, print_characteristics

# name, path, n_observations, n_features
regression_datasets = [
    ('Abalone Train', '../regression/abalone/abalone.trn', 4177, 8),
]

def iterate_regression_dataset_path():
    for name, path, *args in regression_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        yield name, path


def iterate_regression_dataset():
    for name, path, n_observations, n_features in regression_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        x, y = load_svmlight_file(path)
        yield name, x, y, n_observations, n_features


def describe_regression_datasets():
    for name, x, y, *args in iterate_regression_dataset():
        label_mean = np.mean(y)
        label_std = np.std(y)
        label_min = np.min(y)
        label_max = np.max(y)

        characteristics = features_characteristics(x)
        characteristics['label mean'] = '{:.3g}'.format(label_mean)
        characteristics['label std'] = '{:.3g}'.format(label_std)
        characteristics['label min'] = '{:.3g}'.format(label_min)
        characteristics['label max'] = '{:.3g}'.format(label_max)

        print('\n{:}'.format(name))
        print_characteristics(characteristics, html=False)

# describe_regression_datasets()