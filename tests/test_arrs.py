import unittest

from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0), None)

    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([1, 2, 3], -5), [1, 2, 3]
        assert arrs.my_slice([], -5) == []
        assert arrs.my_slice([1, 2, 3], -2), [2, 3]

