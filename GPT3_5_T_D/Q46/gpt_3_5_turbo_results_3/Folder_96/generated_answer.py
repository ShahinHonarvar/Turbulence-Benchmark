
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_1 = gcd(nums[29], nums[74])
    gcd_2 = gcd(gcd_1, nums[49])
    return gcd_2
