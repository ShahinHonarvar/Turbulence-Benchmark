
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    missing_nums = set(range(a + 1, b)) - set(nums[21:200])
    summation = sum(missing_nums)
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]
