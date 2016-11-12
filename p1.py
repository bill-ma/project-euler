#Find the sum of all the multiples of 3 or 5 below 1000.

def sum35(low,high):
	sum=0;
	for i in range(low,high):
		if(i%3==0 or i%5==0):
			sum+=i;
	print(sum);

sum35(1,1000);