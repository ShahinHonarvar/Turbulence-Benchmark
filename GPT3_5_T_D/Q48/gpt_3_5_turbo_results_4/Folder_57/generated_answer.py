
def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    range_nums = set(nums[26:80])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in range_nums:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
