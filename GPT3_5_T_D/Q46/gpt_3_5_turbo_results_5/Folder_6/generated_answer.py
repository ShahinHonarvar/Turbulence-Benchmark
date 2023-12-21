
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]
    return gcd(gcd(num1, num2), num3)
