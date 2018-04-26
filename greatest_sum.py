# Please Pass the Coded Messages
# ==============================

# You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

# You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int list) l = [3, 1, 4, 1]
# Output:
#     (int) 4311

# Inputs:
#     (int list) l = [3, 1, 4, 1, 5, 9]
# Output:
#     (int) 94311



# Take sum of the arr and sort arr reversed
# take modulo with 3 and save diff
# remove the lowest element whose modulo diff is equal to above diff
# if still sum is not divisible by 3 means there is no element whose modulo diff is equal to above diff
# now we remove element whose modulo diff is equal to 3-above diff while sum is not divisble by 3

def concat(numList):
    s = ''.join(map(str, filter(lambda x: x!=None,numList)))
    if s: return int(s)
    if not s: return 0

def answer(arr):
	arr.sort(reverse=True)
	s=sum(arr)
	diff=s%3
	if s>2 and diff:
		for i in range(len(arr)-1,-1,-1):
			if arr[i] and arr[i]%3==diff:
				s-=arr[i]
				arr[i]=None
				break
		while s%3:
			for i in range(len(arr)-1,-1,-1):
				if arr[i] and (arr[i]%3)==(3-diff):
					s-=arr[i]
					arr[i]=None
					break
		
		return concat(arr)		
	elif s>2:
		return concat(arr)
	else:
		return 0				

print answer([3,0,0,0,0,0])
print answer([3,1,1])
print answer([3,3,4])
print answer([3,2,2,1])
