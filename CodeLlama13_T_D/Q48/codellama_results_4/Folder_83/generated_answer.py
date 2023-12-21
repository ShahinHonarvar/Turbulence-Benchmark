
def return_binary_or_hexa(nums):
    a = nums[90] + 1
    b = nums[200] - 1
    result = sum(i for i in range(a, b+1) if i not in nums)
    return hex(result)[2:] if result % 2 else bin(result)[2:]
