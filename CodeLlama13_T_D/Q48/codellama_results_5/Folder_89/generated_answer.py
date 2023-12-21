
def return_binary_or_hexa(nums):
    a, b = nums[55], nums[84]
    total = 0
    for i in range(a + 1, b):
        if i not in nums:
            total += i
    if total % 2 == 0:
        return hex(total)
    else:
        return bin(total)[2:]
