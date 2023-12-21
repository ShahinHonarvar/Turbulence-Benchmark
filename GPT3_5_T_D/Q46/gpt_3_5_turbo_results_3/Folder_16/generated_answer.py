
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(nums[558], nums[110]), nums[628])
