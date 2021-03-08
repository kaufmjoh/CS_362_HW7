def FizzBuzz():

	Total = ""; #This is the running string that will be returned at the end of the function

	for i in range(100):
		
		x = i+1

		Addition = ""; #This is the string that is added to Total, and reset after each loop

		#Determine what the new input to total should be
		if x % 3 == 0 and x % 5 == 0:
			Addition = "FizzBuzz";
		elif x % 3 == 0:
			Addition = "Fizz";
		elif x % 5 == 0:
			Addition = "Buzz";
		else:
			Addition = str(x);

		if x < 100:
			Addition = Addition+", ";

		Total = Total + Addition; #Add a new input to total

	return Total;

