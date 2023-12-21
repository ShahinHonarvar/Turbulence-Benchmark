
def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    range_nums = set(nums[a+1:b])
    sum_nums = sum(i for i in range(a+1, b) if i not in range_nums)
    
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
