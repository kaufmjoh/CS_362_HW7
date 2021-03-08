import unittest
import LeapYear

class TestCaseLeapYear(unittest.TestCase):

	#Test years that are not divisible by 4
	def testNon4MultLeapYears(self):
		self.assertEqual(LeapYear.LeapYear(1), "Not a Leap Year");
		self.assertEqual(LeapYear.LeapYear(2001), "Not a Leap Year");
		self.assertEqual(LeapYear.LeapYear(2021), "Not a Leap Year");


	#Test years that are divisible by 400
	def test400MultLeapYears(self):
		self.assertEqual(LeapYear.LeapYear(400), "Yes a Leap Year");
		self.assertEqual(LeapYear.LeapYear(2000), "Yes a Leap Year");
		self.assertEqual(LeapYear.LeapYear(2400), "Yes a Leap Year");

if __name__ == '__main__':
	unittest.main();
