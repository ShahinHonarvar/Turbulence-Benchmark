
def gcf_three_nums(nums):
    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[49]
    num2 = nums[46]
    num3 = nums[13]

    gcd1 = gcf(num1, num2)
    gcd2 = gcf(gcd1, num3)

    return gcd2
