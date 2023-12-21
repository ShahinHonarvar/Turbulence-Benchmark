
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    excluded_nums = set(nums[57:90])
    sum = 0
    for i in range(a + 1, b):
        if i not in excluded_nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
