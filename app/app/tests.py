"""
Sample test
"""

from django.test import SimpleTestCase

from app import count

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = count.add(5, 6)

        self.assertEqual(res, 11)

    
    def test_subtract_numbers(self):

        res = count.subtract(10,15)

        self.assertEqual(res , 5)
