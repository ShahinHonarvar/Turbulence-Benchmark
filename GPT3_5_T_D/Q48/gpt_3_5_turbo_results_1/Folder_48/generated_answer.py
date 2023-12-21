
def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    valid_nums = set(nums[933:997])
    start = a + 1
    end = b - 1
    sum = 0
    
    for num in range(start, end+1):
        if num not in valid_nums:
            sum += num
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
