
def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[200]
    missing_nums = [num for num in range(a+1, b) if num not in nums[90:201]]
    if len(missing_nums) == 0:
        return ""
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
