
def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[200:203]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
