
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[818]
    num2 = nums[606]
    num3 = nums[873]

    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)

    return gcf
