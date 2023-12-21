
def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    total = 0

    for i in range(a + 1, b):
        if i not in nums[37:43]:
            total += i

    if total == 0:
        return ""

    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
