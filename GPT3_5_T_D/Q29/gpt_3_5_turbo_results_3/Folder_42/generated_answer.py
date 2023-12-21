
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if len(nums) >= 91 and nums[90] > 0 and nums[84] > 0:
        return gcd(nums[90], nums[84])
    else:
        return None
