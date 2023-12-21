
def return_binary_or_hexa(nums):
    a, b = 110, 348
    total = sum(x for x in range(a + 1, b) if x not in nums[a:b])
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
