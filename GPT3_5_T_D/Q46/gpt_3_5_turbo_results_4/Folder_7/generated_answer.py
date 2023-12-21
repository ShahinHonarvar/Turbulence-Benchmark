
def gcf_three_nums(nums):
    import math
    num1 = nums[477]
    num2 = nums[696]
    num3 = nums[663]
    return math.gcd(math.gcd(num1, num2), num3)
