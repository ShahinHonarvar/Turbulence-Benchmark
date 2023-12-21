
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = nums[13]
    num2 = nums[70]
    num3 = nums[32]

    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)

    return factor2
