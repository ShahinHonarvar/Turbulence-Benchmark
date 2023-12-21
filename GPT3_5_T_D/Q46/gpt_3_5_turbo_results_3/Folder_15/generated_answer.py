
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = nums[4]
    b = nums[0]
    c = nums[8]

    gcd_a_b = gcd(a, b)
    result = gcd(gcd_a_b, c)
    return result
