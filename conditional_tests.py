import unittest
from conditional import *

class TestCases(unittest.TestCase):

   # This test here to make sure you named your functions correctly.
   # Any other tests you add should only have one assert per function.
   def test_function_names(self):
      self.assertEqual(max_101(0, 0), 0)
      self.assertEqual(max_of_three(0, 0, 0), 0)
      self.assertEqual(rental_late_fee(0), 0)

   def test_max_101_1(self):
      self.assertEqual(max_101(1,0),1)
   def test_max_101_2(self):   
      self.assertEqual(max_101(3,4),4)

   def test_max_of_three_1(self):
      self.assertEqual(max_of_three(1.0, 0, -1), 1)
   def test_max_of_three_2(self):
      self.assertEqual(max_of_three(2.1, 3.5, 3), 3.5)
   def test_max_of_three_3(self):
      self.assertEqual(max_of_three(4, 6.0, 7), 7)
   def test_max_of_three_4(self):
      self.assertEqual(max_of_three(8, 8, 8), 8)

   def test_rental_late_fee_1(self):
      self.assertEqual(rental_late_fee(0), 0)
   def test_rental_late_fee_2(self):
      self.assertEqual(rental_late_fee(8), 5)
   def test_rental_late_fee_3(self):
      self.assertEqual(rental_late_fee(15), 7)
   def test_rental_late_fee_4(self):
      self.assertEqual(rental_late_fee(24), 19)
   def test_rental_late_fee_5(self):
      self.assertEqual(rental_late_fee(30), 100)
      
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

