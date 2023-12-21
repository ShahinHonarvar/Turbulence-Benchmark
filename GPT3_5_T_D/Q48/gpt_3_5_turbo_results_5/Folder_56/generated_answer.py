
def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    nums_range = set(nums[a+1:b])
    result = sum([i for i in range(a+1, b) if i not in nums_range])
    
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]
