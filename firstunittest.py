import simpleprogram
import unittest

class TestPower(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(simpleprogram.power(2, 2), 4)

if __name__ == '__main__':
    unittest.main()