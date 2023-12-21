
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    total_sum = 0
    for i in range(a+1, b):
        if i not in nums[20:201]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
