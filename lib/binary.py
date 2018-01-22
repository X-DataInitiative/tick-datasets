import os

import numpy as np
from sklearn.datasets import load_svmlight_file

from lib.dataset_analysis import features_characteristics, print_characteristics

# name, path, n_observations, n_features
binary_datasets = [
    ('Adult Train', '../binary/adult/adult.trn.bz2', 32561, 123),
    ('Adult Test', '../binary/adult/adult.tst.bz2', 16281, 123),
    ('Covtype Train', '../binary/covtype/covtype.trn.bz2', 581012, 54),
    ('ijcnn1 Train', '../binary/ijcnn1/ijcnn1.trn.bz2', 49990, 22),
    ('ijcnn1 Test', '../binary/ijcnn1/ijcnn1.tst.bz2', 91701, 22),
    ('Reuters Train', '../binary/reuters/reuters.trn.bz2', 7770, 8315),
    ('Reuters Test', '../binary/reuters/reuters.tst.bz2', 3299, 8315),
    ('KDD 2010 Train', '../binary/kdd2010/kdd2010.trn.bz2',
     19264097, 1129522),
    ('KDD 2010 Test', '../binary/kdd2010/kdd2010.tst.bz2',
     748401, 1163024),
]


def iterate_binary_dataset_path():
    for name, path, *args in binary_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        yield name, path


def iterate_binary_dataset():
    for name, path, n_observations, n_features in binary_datasets:
        path = os.path.join(os.path.dirname(__file__), path)
        x, y = load_svmlight_file(path)
        yield name, x, y, n_observations, n_features


def describe_binary_datasets():
    for name, x, y, *args in iterate_binary_dataset():
        n_rows = x.shape[0]
        positive_ratio = np.sum(y == 1) / n_rows

        characteristics = features_characteristics(x)
        characteristics['Class balancing'] = '{:.3g}% positive samples'.format(
            positive_ratio * 100)

        print('\n{:}'.format(name))
        print_characteristics(characteristics, html=False)
