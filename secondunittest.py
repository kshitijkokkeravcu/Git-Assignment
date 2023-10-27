import simpleprogram
import unittest

class TestPower(unittest.TestCase):
    def test_char(self):
        with self.assertRaises(TypeError):
            simpleprogram.power("a", "b")

if __name__ == '__main__':
    unittest.main()