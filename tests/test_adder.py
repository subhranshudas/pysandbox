import unittest
from pysandbox.adder import add, addBy100

class AdderTest(unittest.TestCase):

    def test_add_should_add_two_numbers(self):
        a = 20
        b = 40
        self.assertEqual(add(a, b), 60)

    def test_add_by_100_should_add_100(self):
        a = 40
        b = 80
        self.assertEqual(addBy100(a, b), 220)
    

if __name__ == "__main__":
    unittest.main()
