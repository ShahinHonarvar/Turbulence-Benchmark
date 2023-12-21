
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[66]
    num2 = nums[90]
    num3 = nums[27]

    gcf_1_2 = gcd(num1, num2)
    gcf_1_3 = gcd(num1, num3)
    gcf_2_3 = gcd(num2, num3)

    result = gcd(gcf_1_2, gcf_1_3, gcf_2_3)
    return result
