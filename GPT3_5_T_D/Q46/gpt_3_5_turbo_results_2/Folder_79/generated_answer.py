
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcd(gcd(nums[16], nums[87]), nums[95])
