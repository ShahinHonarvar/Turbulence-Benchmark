
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]

    gcd_num1_num2 = gcd(num1, num2)
    gcf_three_nums = gcd(gcd_num1_num2, num3)

    return gcf_three_nums
