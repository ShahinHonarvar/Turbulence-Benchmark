
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[78]

    total_sum = sum(nums[a + 1:b])

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
