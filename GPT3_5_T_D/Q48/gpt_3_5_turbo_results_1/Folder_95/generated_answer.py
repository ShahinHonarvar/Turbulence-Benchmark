
def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]

    total_sum = sum(nums[a+1:b])

    if all(x in nums[32:99] for x in range(a+1, b)):
        return ""

    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
