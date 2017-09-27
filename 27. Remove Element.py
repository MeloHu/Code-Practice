'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''


nums = [3,2,3,7,4,6,3,3]
val = 3

length = len(nums)
cursor = length -1 

for i in range(length-1,-1,-1):
    if nums[i] != val:
        cursor = i
        break
range_loop = cursor +1
for k in range(range_loop):
    if k <= cursor:
        if nums[k] == val:
            nums[k] = nums[cursor]
            cursor -= 1

nums = nums[:cursor+1]
newlength = len(nums)

print(nums)
print(newlength)
