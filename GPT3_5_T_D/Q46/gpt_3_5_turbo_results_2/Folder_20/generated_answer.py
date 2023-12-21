
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[29]
    num2 = nums[53]
    num3 = nums[42]

    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)

    return gcf2
