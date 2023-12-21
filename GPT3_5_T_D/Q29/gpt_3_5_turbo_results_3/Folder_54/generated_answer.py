
def gcf_two_nums(nums):
    a = nums[56]
    b = nums[92]
    while b:
        a, b = b, a % b
    return a
