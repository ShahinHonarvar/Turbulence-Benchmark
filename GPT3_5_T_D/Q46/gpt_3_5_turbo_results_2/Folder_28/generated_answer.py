
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    gcf_1_2 = gcd(num1, num2)
    gcf = gcd(gcf_1_2, num3)
    return gcf
