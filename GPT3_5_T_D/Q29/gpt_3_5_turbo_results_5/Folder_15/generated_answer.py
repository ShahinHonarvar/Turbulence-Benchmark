
def gcf_two_nums(nums):
    a, b = nums[0], nums[1]
    while b:
        a, b = b, a % b
    return a
