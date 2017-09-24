'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

s = '(){}[{()'

length = len(s)
i = 0
pool = ["()", "{}","[]"]

while i < length:
	sign = 0
	for k in pool:
		if s[i]+s[i+1] == k:
			i += 2
			sign = 1
			break
	if sign == 0:
		print("No")
		exit()
print("Yes")
