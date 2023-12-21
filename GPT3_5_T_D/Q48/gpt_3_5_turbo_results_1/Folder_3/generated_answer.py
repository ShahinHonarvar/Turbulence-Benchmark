
def return_binary_or_hexa(nums):
    if all(num in nums[56:89] for num in range(nums[56] + 1, nums[88])):
        return ""
    total_sum = sum(num for num in range(nums[56] + 1, nums[88]) if num not in nums[56:89])
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]
