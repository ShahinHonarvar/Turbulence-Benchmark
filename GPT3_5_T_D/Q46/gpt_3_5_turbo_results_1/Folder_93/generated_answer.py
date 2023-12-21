
def gcf_three_nums(nums):
    num1 = nums[25]
    num2 = nums[76]
    num3 = nums[57]

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcf = gcd(num1, gcd(num2, num3))
    return gcf
