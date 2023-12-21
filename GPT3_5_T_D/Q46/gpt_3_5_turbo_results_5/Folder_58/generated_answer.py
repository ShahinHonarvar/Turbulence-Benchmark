
def gcf_three_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = nums[145]
    num2 = nums[183]
    num3 = nums[770]

    gcd_ab = gcd(num1, num2)
    return gcd(gcd_ab, num3)
