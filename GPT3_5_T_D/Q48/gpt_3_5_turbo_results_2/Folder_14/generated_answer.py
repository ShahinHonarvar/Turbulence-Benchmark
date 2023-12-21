
def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    total_sum = 0
    for i in range(a+1, b):
        if i not in nums[2:6]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
