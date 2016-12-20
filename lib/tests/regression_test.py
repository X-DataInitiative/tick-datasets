import unittest

from lib.regression import iterate_regression_dataset


class RegressionTests(unittest.TestCase):
    def test_data_set_consistency(self):
        """...Test regression datasets have the expected shape
        """
        for name, x, y, n_observations, n_features in \
                iterate_regression_dataset():
            self.assertEqual(x.shape[0], n_observations,
                             "Incorrect number of observations in %s" % name)
            self.assertEqual(y.shape[0], n_observations,
                             "Incorrect number of labels in %s" % name)
            self.assertEqual(x.shape[1], n_features,
                             "Incorrect number of features in %s" % name)


if __name__ == '__main__':
    unittest.main()
