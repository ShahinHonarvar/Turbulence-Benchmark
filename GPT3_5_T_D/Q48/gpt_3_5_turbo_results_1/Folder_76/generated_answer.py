
def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    num_set = set(nums[451:905])
    
    sum = 0
    for i in range(a+1, b):
        if i not in num_set:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
