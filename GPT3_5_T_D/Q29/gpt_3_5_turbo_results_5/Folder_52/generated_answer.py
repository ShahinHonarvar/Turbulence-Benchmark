
def gcf_two_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    num_1 = nums[90]
    num_2 = nums[41]
    return gcd(num_1, num_2)
