
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[3]
    total_sum = 0

    for i in range(a + 1, b):
        if i not in nums[1:3]:
            total_sum += i

    if total_sum == 0:
        return ""

    if total_sum % 2 != 0:
        return bin(total_sum)[2:]

    return hex(total_sum)[2:]
