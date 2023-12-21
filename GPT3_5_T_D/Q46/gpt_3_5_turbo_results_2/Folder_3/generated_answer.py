
def gcf_three_nums(nums):
    import math
    num1 = nums[31]
    num2 = nums[69]
    num3 = nums[40]
    return math.gcd(math.gcd(num1, num2), num3)
