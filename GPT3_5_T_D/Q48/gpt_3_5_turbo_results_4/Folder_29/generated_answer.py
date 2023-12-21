
def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    num_set = set(nums[71:98])
    
    sum_val = sum(i for i in range(a+1, b) if i not in num_set)
    
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]
