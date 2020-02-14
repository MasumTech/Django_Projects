# Authour Masum Reza
# --------------------------
#      Unit Test
# --------------------------


import unittest

from Unittesting import msmath
from Unittesting import msstring


class MsPackMsMathTestCase(unittest.TestCase):
    def test_sum(self):
        sum = msmath.sum(10, 40)
        self.assertEqual(sum, 50)

    def test_subtract(self):
        result = msmath.subtract(120,20)
        self.assertTrue(result==100)

    def test_multiplication(self):
        result = msmath.multiplication(5,6)
        self.assertEqual(result, 30)

    def test_division(self):
        result = msmath.division(50,5)
        self.assertEqual(result, 10)


class MsPackMsStringTestCase(unittest.TestCase):
    def setUp(self):
        self.str_obj = msstring.MsName("Life", "is Good")

    def test_full_name(self):
        #name = msstring.MsName("Life", "is Good").full_name()
        name = self.str_obj.full_name()
        self.assertEqual(name, "Life is Good")

    def test_full_name_length(self):
        length = len(self.str_obj.full_name())
        self.assertTrue(length == 12)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
