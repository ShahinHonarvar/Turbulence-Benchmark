
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    total_sum = 0

    for i in range(a + 1, b):
        if nums.index(i) < 56 or nums.index(i) > 90:
            total_sum += i

    if total_sum == 0:
        return ''

    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
