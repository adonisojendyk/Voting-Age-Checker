print("***Voting Age Checker***")

age = int(input("What is your age?"))
gap = 18-age

if age >=18:
	print("You are old enough to vote.")
elif gap == 1:
	print("You are not old enough to vote. You have " + str(gap) + " year till you can vote.")
else:
	print("You are not old enough to vote. You have " + str(gap) + " years till you can vote.")
