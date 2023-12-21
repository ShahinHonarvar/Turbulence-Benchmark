
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[78]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in nums[44:79]:
            sum_val += i
    if sum_val == 0:
        return ""
    elif sum_val % 2 != 0:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
