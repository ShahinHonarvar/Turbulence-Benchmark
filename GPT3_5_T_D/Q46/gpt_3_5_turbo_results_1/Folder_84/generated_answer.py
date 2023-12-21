
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = nums[695]
    num2 = nums[710]
    num3 = nums[914]

    gcd1 = gcd(num1, num2)
    result = gcd(gcd1, num3)

    return result
