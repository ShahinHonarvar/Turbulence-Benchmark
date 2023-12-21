
def gcf_three_nums(nums):
    import math
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    return math.gcd(math.gcd(num1, num2), num3)
