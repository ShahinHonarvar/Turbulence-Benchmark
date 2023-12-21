
def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    total_sum = sum(nums[a+1:b])
    if all(num in nums[a:b+1] for num in range(a+1, b)):
        return ""
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
