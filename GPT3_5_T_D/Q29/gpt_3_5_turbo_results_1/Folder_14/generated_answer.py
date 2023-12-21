
def gcf_two_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num_49 = nums[49]
    num_53 = nums[53]
    return gcd(num_49, num_53)
