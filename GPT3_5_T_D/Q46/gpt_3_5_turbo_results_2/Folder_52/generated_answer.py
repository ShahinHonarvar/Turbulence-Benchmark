
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]

    gcd_nums = gcd(gcd(num1, num2), num3)
    return gcd_nums
