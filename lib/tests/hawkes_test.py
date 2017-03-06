import unittest

from lib.hawkes import iterate_hawkes_dataset


class HawkesTests(unittest.TestCase):
    def test_data_set_consistency(self):
        """...Test hawkes datasets have the expected shape
        """
        for name, timestamps_list, n_realizations in iterate_hawkes_dataset():
            self.assertEqual(len(timestamps_list), n_realizations,
                             "Incorrect number of realizations in %s" % name)

if __name__ == '__main__':
    unittest.main()
