
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    sum = 0
    
    for i in range(a+1, b):
        if i not in nums[10:76]:
            sum += i
    
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]
