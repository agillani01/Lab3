import unittest
from logic import *

class TestCases(unittest.TestCase):

   # This test here to make sure you named your functions correctly.
   # Any other tests you add should only have one assert per function.
   def test_function_names(self):
      self.assertTrue(is_even(0))
      self.assertFalse(in_an_interval(0))

   def test_is_even_1(self):
      self.assertTrue(is_even(2))
   def test_is_even_2(self):
      self.assertFalse(is_even(3))

   def test_im_an_interval_1(self):
      self.assertFalse(in_an_interval(1))
   def test_im_an_interval_2(self):
      self.assertTrue(in_an_interval(2))
   def test_im_an_interval_3(self):
      self.assertFalse(in_an_interval(9))
   def test_im_an_interval_4(self):
      self.assertTrue(in_an_interval(19))
   def test_im_an_interval_5(self):
      self.assertTrue(in_an_interval(50))
   def test_im_an_interval_6(self):
      self.assertTrue(in_an_interval(101))
   def test_im_an_interval_7(self):
      self.assertFalse(in_an_interval(104))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

