import unittest

import numpy as np

from lib.binary import iterate_binary_dataset


class BinaryTests(unittest.TestCase):
    def test_data_set_consistency(self):
        """...Test binary dataset have the expected shape
        """
        for name, x, y, n_observations, n_features in \
                iterate_binary_dataset():
            self.assertEqual(x.shape[0], n_observations,
                             "Incorrect number of observations in %s" % name)
            self.assertEqual(y.shape[0], n_observations,
                             "Incorrect number of labels in %s" % name)
            self.assertEqual(x.shape[1], n_features,
                             "Incorrect number of features in %s" % name)

            self.assertEqual(set(np.unique(y)), {-1, 1},
                             "Incorrect labels encoding in %s" % name)


if __name__ == '__main__':
    unittest.main()
