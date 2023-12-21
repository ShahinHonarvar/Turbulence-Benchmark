
def gcf_three_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = nums[1]
    num2 = nums[6]
    num3 = nums[8]

    common_factor = gcd(gcd(num1, num2), num3)
    return common_factor
