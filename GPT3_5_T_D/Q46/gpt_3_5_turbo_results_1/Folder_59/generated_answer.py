
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(nums[7], nums[6]), nums[8])
