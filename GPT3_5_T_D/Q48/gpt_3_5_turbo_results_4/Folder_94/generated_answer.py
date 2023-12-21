
def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    total_sum = 0

    for i in range(a + 1, b):
        if i not in nums[43:87]:
            total_sum += i

    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ""
    else:
        return hex(total_sum)[2:].upper()
