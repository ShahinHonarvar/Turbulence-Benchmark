
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    total_sum = 0
    for num in range(a+1, b):
        if num not in nums[20:37]:
            total_sum += num
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
