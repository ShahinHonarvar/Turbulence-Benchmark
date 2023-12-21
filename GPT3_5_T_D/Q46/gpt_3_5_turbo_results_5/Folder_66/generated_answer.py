
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = nums[92]
    b = nums[69]
    c = nums[95]

    return gcd(gcd(a, b), c)
