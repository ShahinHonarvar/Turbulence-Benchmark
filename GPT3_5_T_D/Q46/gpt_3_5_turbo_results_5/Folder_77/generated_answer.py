
def gcf_three_nums(nums):
    import math
    a = nums[693]
    b = nums[331]
    c = nums[668]
    return math.gcd(math.gcd(a, b), c)
