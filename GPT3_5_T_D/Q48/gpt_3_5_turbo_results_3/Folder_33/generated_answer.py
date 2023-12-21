
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    total = 0

    for i in range(a + 1, b):
        if i not in nums[13:35]:
            total += i

    if total == 0:
        return ""

    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
