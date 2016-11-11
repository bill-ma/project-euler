import random

low = 1;
high = 100;

x = random.randrange(low,high);
#print(x);
print("I'm thinking of a number b/t", low, "and", high, end="\n\n");

count = 1;

while True:
	print("Attempt #", count, end=": ");
	guess = int(input());

	if(guess < x):
		print("Too low!");
	elif(guess > x):
		print("Too high!");
	else:
		print("Correct!");
		break;
	count+=1;
