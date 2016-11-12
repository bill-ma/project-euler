#largest palindrome that's a product of two 3-digit numbers

def isPalindrome(x):
	return str(x) == str(x)[::-1]

def solution():
	largest = 0;
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			if isPalindrome(i*j):
				if(i*j > largest):
					largest = i*j
					print(i,j)
	return largest

print(solution())
