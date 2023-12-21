
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    total_sum = sum([i for i in range(a + 1, b) if i not in nums[1:4]])
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
