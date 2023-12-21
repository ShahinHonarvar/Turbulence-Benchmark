
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    if b - a <= 1:
        return ""

    num_sum = 0
    for num in range(a + 1, b):
        if num not in nums[44:68]:
            num_sum += num

    if num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:].upper()
