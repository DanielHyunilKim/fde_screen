import unittest
from solution import sort


class TestSolution(unittest.TestCase):

    def test_standard(self):
        width, height, length, mass = 50, 50, 50, 10
        self.assertEqual(sort(width, height, length, mass), 'STANDARD')

    def test_heavy(self):
        width, height, length, mass = 50, 50, 50, 30
        self.assertEqual(sort(width, height, length, mass), 'SPECIAL')

    def test_bulky(self):
        width, height, length, mass = 500, 500, 500, 10
        self.assertEqual(sort(width, height, length, mass), 'SPECIAL')

    def test_rejected(self):
        width, height, length, mass = 500, 500, 500, 30
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')

    def test_string_input_1(self):
        width, height, length, mass = '50', '50', '50', '10'
        self.assertEqual(sort(width, height, length, mass), 'STANDARD')

    def test_string_input_2(self):
        width, height, length, mass = '50.5', '50.5', '50.5', '10'
        self.assertEqual(sort(width, height, length, mass), 'STANDARD')

    def test_null_input(self):
        width, height, length, mass = '50.5', '50.5', '50.5', None
        self.assertEqual(sort(width, height, length, mass), 'INVALID INPUT')

    def test_non_numeric_input(self):
        width, height, length, mass = '50.5', '50.5', '50.5', 'Ten'
        self.assertEqual(sort(width, height, length, mass), 'INVALID INPUT')


if __name__ == '__main__':
    unittest.main()
