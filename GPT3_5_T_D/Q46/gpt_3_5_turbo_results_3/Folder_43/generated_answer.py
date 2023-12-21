
def gcf_three_nums(nums):
    import math
    num1 = nums[33]
    num2 = nums[78]
    num3 = nums[93]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf
