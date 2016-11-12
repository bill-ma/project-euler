# What is the largest prime factor of the number 600851475143?
from math import sqrt

def isPrime(x):
	for i in range(2,int(sqrt(x)+1)):
		if(x%i == 0):
			return False
	return True

def LargestPrimeFactor(x):
	for i in range(x//2+1,1,-1):
		if(x%i == 0):
			if(isPrime(i)):
				print(i)
				break;
		else: 
			continue

#print(isPrime(600851475143))
#listPrimeFactors(13195)
#listPrimeFactors(600851475143)
#hello1