
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(nums[38], nums[52]), nums[69])
