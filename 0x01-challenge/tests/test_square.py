import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s = Square(5)
    def test_area(self):
        self.assertEqual(self.s.area(), 25)
    def test_perimeter(self):
        self.assertEqual(self.s.perimeter(), 20)
    def test_invalid_side_length(self):
        with self.assertRaises(ValueError):
            Square(-1)

if __name__ == "__main__":
    unittest.main()
