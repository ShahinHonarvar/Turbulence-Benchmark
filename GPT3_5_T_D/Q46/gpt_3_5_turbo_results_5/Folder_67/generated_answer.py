
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcd(gcd(nums[70], nums[41]), nums[20])
