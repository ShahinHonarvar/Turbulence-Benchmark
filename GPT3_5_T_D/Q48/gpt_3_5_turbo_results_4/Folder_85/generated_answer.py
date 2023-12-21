
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    total_sum = sum(range(a + 1, b))
    missing_nums = [num for num in range(a + 1, b) if num not in nums[1:9]]
    
    if len(missing_nums) == 0:
        return ''
    
    result = total_sum % 2
    
    if result == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
