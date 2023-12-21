
def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[45:49]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
