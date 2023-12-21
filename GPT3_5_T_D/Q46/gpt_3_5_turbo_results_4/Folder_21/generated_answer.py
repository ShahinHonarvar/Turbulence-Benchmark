
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    gcf_1_2 = gcd(num1, num2)
    gcf_1_2_3 = gcd(gcf_1_2, num3)
    return gcf_1_2_3
