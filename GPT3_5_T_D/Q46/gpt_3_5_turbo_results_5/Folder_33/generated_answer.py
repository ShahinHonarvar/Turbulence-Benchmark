
def gcf_three_nums(nums):
    from math import gcd
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]

    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)

    return gcf
