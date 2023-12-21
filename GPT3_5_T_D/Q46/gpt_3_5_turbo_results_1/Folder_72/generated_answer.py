
def gcf_three_nums(nums):
    import math
    num1 = nums[44]
    num2 = nums[91]
    num3 = nums[42]
    return math.gcd(math.gcd(num1, num2), num3)
