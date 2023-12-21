
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[2]
    total = 0
    for i in range(a + 1, b):
        if i not in nums:
            total += i
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
