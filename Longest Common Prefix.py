strs = ['hibc','hidf','hihh','haj']
str1 = strs[0]
k = 0

for i in range(len(strs)):
    while k < len(str1) and str1:
        if strs[i][k] == str1[k]:
            k += 1
        else:
            if k-1 >= 0:
                str1 = str1[:k]
            else:
                str1 = ''
    k = 0

print("fianl",str1)

