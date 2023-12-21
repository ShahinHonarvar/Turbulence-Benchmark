
def return_binary_or_hexa(nums):
    a = nums[35]
    b = nums[64]
    total_sum = sum([i for i in range(a+1, b) if i not in nums[35:65]])
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ""
    else:
        return hex(total_sum)[2:]
