
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    missing_nums = set(range(a + 1, b)) - set(nums[1:7])
    if len(missing_nums) == 0:
        return ""
    summation = sum(missing_nums)
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]
