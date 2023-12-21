
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = nums[31]
    b = nums[69]
    c = nums[40]
    gcf = gcd(a, gcd(b, c))
    return gcf
