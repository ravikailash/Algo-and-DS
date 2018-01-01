'''
Given a rotated sorted array, find the smallest element in the array
'''

import unittest


def find_minimum(arr, low, high):
    if low > high:
        return arr[0], 0

    if low == high:
        return arr[low], low

    mid = (low + high) // 2

    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1], mid+1

    if mid > low and arr[mid] < arr[mid-1]:
        return arr[mid], mid

    if arr[high] > arr[mid]:
        return find_minimum(arr, low, mid-1)

    return find_minimum(arr, mid+1, high)


class TestSmallestInRotatedArray(unittest.TestCase):
    def test_finding_minimum(self):
        test_arrays = [[5, 6, 1, 2, 3, 4],
                       [1, 2, 3, 4],
                       [2, 3, 4, 1],
                       [5, 6, 7, 8, 9, 2, 3]]

        result = [(1, 2), (1, 0), (1, 3), (2, 5)]

        for array, output in zip(test_arrays, result):
            res = find_minimum(array, 0, len(array)-1)
            print('{} -> {}'.format(array, res))
            self.assertTrue(res == output)


if __name__ == "__main__":
    unittest.main(verbosity=2)