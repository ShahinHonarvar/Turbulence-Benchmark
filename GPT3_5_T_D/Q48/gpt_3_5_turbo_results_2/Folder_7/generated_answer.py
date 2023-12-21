
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    
    sum = 0
    for i in range(a+1, b):
        if i not in nums[10:97]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
