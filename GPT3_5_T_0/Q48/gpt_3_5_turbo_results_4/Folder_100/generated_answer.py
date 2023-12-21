
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[78]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[44:78]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
