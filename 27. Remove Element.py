
nums = [3,2,3,7,4,6,1,3]
val = 3

length = len(nums)
cursor = length -1 
delet = 0

for i in range(length-1,-1,-1):
    if nums[i] != val:
        cursor = i
        break
    else:                
        delet += 1
range_loop = cursor +1
for k in range(range_loop):
    if k <= cursor:
        if nums[k] == val:
            nums[k] = nums[cursor]
            cursor -= 1
            delet += 1

left = length - delet            
nums = nums[:left]
newlength = len(nums)

print(nums)
print(newlength)