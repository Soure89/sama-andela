import unittest

from divide import divide_two_numbers

class Testdivision(unittest.TestCase):
	def test_correct_answers(self):
		self.assertEqual(divide_two_numbers(20,5), 4)
	def test_correct_answers_1(self):
		self.assertEqual(divide_two_numbers(-10,5),-2)
	def test_correct_answers_2(self):
		self.assertEqual(divide_two_numbers(-30,5),-6)
	def test_correct_answers_3(self):
		self.assertEqual(divide_two_numbers(40,5),8)	







if __name__=='__main__':
	unittest.main()






