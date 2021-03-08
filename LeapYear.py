def LeapYear(x):

	if x % 4 != 0:
		return ("Not a Leap Year");
	elif x % 400 == 0:
		return ("Yes a Leap Year");
	elif x % 100 == 0:
		return ("Not a Leap Year");
