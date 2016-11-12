# What is the largest prime factor of the number 600851475143?

from math import sqrt

def isPrime(x):
	for i in range(2,int(sqrt(x)+1)):
		if(x%i == 0):
			return False
	return True

def largestPrimeFactor(x):
	for i in range(x//2+1,1,-1):
		if(x%i == 0):
			if(isPrime(i)):
				print(i)
				break;

largestPrimeFactor(600851475143)

"""
#better solution
def solution3(N=600851475143):
    p = 2
    while N > 1:
        while not N % p:
            N //= p
        p += 1
    return p - 1

print(solution3())
"""