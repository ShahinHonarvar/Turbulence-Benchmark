
def gcf_two_nums(nums):
    a = nums[90]
    b = nums[84]
    while b != 0:
        a, b = b, a % b
    return a
