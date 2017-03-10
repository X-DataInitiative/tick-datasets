import unittest

from lib.hawkes import iterate_hawkes_dataset


class HawkesTests(unittest.TestCase):
    def test_data_set_consistency(self):
        """...Test hawkes datasets have the expected shape
        """
        for name, timestamps_list, n_realizations, n_nodes, end_time in \
                iterate_hawkes_dataset():
            self.assertEqual(len(timestamps_list.keys()), n_realizations,
                             "Incorrect number of realizations in %s" % name)

            for name, timestamps in timestamps_list.items():
                self.assertEqual(timestamps.shape, (n_nodes,),
                                 "Incorrect number of nodes in %s" % name)
                fist_time = min(map(min, timestamps))
                self.assertGreaterEqual(fist_time, 0,
                                        "Incorrect first time in %s" % name)
                last_time = max(map(max, timestamps))
                self.assertLessEqual(last_time, end_time,
                                     "Incorrect last time in %s" % name)


if __name__ == '__main__':
    unittest.main()
