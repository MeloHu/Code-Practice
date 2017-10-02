'''
Given two binary strings, return their sum (also a binary string).
'''


a = "11"
b = "111"


str0 = ""
carry = 0
if len(a) > len(b):
    str1 = a
    str2 = b 
else:
    str1 = b 
    str2 = a

k = len(str2)-1    
for i in range(len(str1)-1,-1,-1):
    if k>=0:
        sum0 = int(str1[i]) + int(str2[k]) + carry
        k-=1
    else:
        sum0 = int(str1[i]) + 0 + carry
    if sum0 > 1:
    	sum0 -= 2
        carry = 1
    else:
        carry = 0
    
    str0 = str(sum0) + str0
if carry != 0:
    str0 = "1" + str0
print(str0)