
def gcf_two_nums(nums):
    a = nums[184]
    b = nums[307]
    while b != 0:
        a, b = b, a % b
    return a
