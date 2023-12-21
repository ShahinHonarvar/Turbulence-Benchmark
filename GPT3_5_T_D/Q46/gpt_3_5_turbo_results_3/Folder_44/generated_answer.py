
def gcf_three_nums(nums):
    import math
    num1 = nums[62]
    num2 = nums[96]
    num3 = nums[26]
    return math.gcd(math.gcd(num1, num2), num3)
