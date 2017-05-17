import unittest
import numpy as np

from lib.hawkes import iterate_hawkes_dataset


def detect_duplicates(timestamps):
    """Detect if one timestamp appears twice in the realisation
    
    Parameters
    ----------
    timestamps : `list` of `np.ndarray`
        Hawkes realization
        
    Returns
    -------
    output : `bool`
        True if a timestamp appears twice
    """
    detected = False
    n_nodes = len(timestamps)

    # Search for timestamps appearing twice in the same node
    for i in range(n_nodes):
        diff = timestamps[i][1:] - timestamps[i][:-1]
        mask = np.hstack((True, diff != 0))
        detected |= not np.alltrue(mask)

    # Search for timestamps appearing twice in two different nodes
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            search_left_i = np.searchsorted(timestamps[j], timestamps[i],
                                            side='left')
            search_right_i = np.searchsorted(timestamps[j], timestamps[i],
                                             side='right')

            search_left_j = np.searchsorted(timestamps[i], timestamps[j],
                                            side='left')
            search_right_j = np.searchsorted(timestamps[i], timestamps[j],
                                             side='right')

            detected |= not np.alltrue(search_left_i == search_right_i)
            detected |= not np.alltrue(search_left_j == search_right_j)

    return detected


class HawkesTests(unittest.TestCase):
    def test_detect_duplicates(self):
        """...Test that test function works as expected
        """
        timestamps = [np.array([1., 2., 3.])]
        self.assertFalse(detect_duplicates(timestamps))

        timestamps = [np.array([1., 2., 2., 3.])]
        self.assertTrue(detect_duplicates(timestamps))

        timestamps = [np.array([1., 2., 3.]),
                      np.array([4., 5., 6., 7.])]
        self.assertFalse(detect_duplicates(timestamps))

        timestamps = [np.array([1., 2., 3.]),
                      np.array([4., 5., 6., 6., 7.])]
        self.assertTrue(detect_duplicates(timestamps))

        timestamps = [np.array([1., 2., 4.]),
                      np.array([4., 5., 6., 7.])]
        self.assertTrue(detect_duplicates(timestamps))

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

                self.assertFalse(detect_duplicates(timestamps))


if __name__ == '__main__':
    unittest.main()
