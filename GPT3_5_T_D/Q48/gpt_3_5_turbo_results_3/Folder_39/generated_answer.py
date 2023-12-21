
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[91]
    range_sum = sum([i for i in range(a + 1, b) if i not in nums[44:92]])

    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
