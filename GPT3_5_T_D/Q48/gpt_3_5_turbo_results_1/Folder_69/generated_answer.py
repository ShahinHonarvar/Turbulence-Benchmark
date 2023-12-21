
def return_binary_or_hexa(nums):
    a = nums[39]
    b = nums[43]
    total = 0

    for num in range(a + 1, b):
        if num not in nums[39:44]:
            total += num

    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ""
    else:
        return hex(total)[2:]
