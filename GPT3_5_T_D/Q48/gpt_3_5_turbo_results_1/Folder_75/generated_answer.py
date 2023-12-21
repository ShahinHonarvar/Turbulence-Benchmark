
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[51]
    
    missing_nums = [num for num in range(a + 1, b) if num not in nums[20:51]]
    if missing_nums == []:
        return ""
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    
    return hex(sum_missing_nums)[2:]
