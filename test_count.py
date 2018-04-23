import unittest
from count import count


class CountTestCase(unittest.TestCase):
    def test_empty_list(self):
        test_list = []
        result = count(test_list)
        expects = len(test_list)

        assert expects == result, 'Expected {} but got {}'.format(
            expects, result)

    def test_small_list(self):
        test_list = list(range(10))
        result = count(test_list)
        expects = len(test_list)

        assert expects == result, 'Expected {} but got {}'.format(
            expects, result)

    def test_big_list(self):
        test_list = list(range(5436891))
        result = count(test_list)
        expects = len(test_list)

        assert expects == result, 'Expected {} but got {}'.format(
            expects, result)


if __name__ == '__main__':
    unittest.main()
