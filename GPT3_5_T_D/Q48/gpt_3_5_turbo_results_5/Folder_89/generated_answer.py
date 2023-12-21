
def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    total_sum = 0

    for i in range(a + 1, b):
        if i not in nums[55:85]:
            total_sum += i

    if total_sum % 2 == 0:
        return hex(total_sum).lstrip("0x")
    else:
        return bin(total_sum).lstrip("0b")
