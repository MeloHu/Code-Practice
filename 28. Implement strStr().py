'''Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. '''



haystack = 'abcdefghij'
needle = 'de'

res = 0
cursor = 0
for i in range(len(haystack)):
	if haystack[i] == needle[0]:
		res = i
		cursor = i 
		for k in range(1,len(needle)):
			cursor += 1
			if haystack[cursor] != needle[k]:
				break
			else: 
				if k == len(needle)-1:
					print(res)
					exit()
print(-1) 
