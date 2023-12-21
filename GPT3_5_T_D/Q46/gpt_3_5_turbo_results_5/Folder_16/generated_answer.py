
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = nums[558]
    num2 = nums[110]
    num3 = nums[628]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf
