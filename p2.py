"""
Description:
By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""
#cleaner code after looking at other people's solution
def fibbEven(maximum):
	x,x_prev,my_sum=1,0,0
	while(x<maximum):
		if(x % 2 == 0):
			my_sum += x
		x,x_prev = x+x_prev,x
	return my_sum
print(fibbEven(4000000))

#how I originally solved it
"""
import sys
def fib(prev,curr,totalEven,last):
	next_ = prev + curr;
	if(next_%2 == 0):
		totalEven += next_;

	if(next_ > last):
		print(totalEven);
		sys.exit();
	else:
		#print(next_, end=" ");
		fib(curr,next_,totalEven,last);

fib(0,1,0,4000000);
"""

