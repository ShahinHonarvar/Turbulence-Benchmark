
def return_binary_or_hexa(nums):
    a = nums[20] + 1
    b = nums[200] - 1
    result = sum(filter(lambda x: x not in nums, range(a, b+1)))
    if result % 2 == 0:
        return hex(result)
    else:
        return bin(result)[2:]
