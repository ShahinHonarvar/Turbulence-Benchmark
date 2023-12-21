
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = nums[13]
    b = nums[76]
    c = nums[44]

    result = gcd(gcd(a, b), c)
    return result
