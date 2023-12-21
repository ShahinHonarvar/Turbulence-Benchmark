
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd1 = gcd(nums[654], nums[312])
    gcd2 = gcd(gcd1, nums[441])
    return gcd2
