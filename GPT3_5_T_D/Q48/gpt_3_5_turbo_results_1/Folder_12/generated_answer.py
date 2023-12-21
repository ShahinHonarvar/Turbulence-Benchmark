
def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    sum_val = sum([i for i in range(a + 1, b) if i not in nums[16:88]])
    
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
