
def gcf_two_nums(nums):
    a = nums[88]
    b = nums[35]
    while b:
        a, b = b, a % b
    return a
