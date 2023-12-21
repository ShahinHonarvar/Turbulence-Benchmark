
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd_1 = gcd(nums[1], nums[2])
    gcd_2 = gcd(gcd_1, nums[7])
    return gcd_2
