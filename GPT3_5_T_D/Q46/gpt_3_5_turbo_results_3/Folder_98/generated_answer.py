
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if len(nums) >= 9:
        return gcd(gcd(nums[8], nums[2]), nums[1])
    else:
        return None
