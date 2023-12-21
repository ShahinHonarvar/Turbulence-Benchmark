
def return_binary_or_hexa(nums):
    a = nums[49]
    b = nums[74]
    missing_nums = [num for num in range(a+1, b) if num not in nums[49:75]]
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
