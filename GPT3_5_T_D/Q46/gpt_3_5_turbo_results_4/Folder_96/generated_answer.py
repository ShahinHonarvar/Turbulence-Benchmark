
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num_1 = nums[29]
    num_2 = nums[74]
    num_3 = nums[49]

    gcd_1 = gcd(num_1, num_2)
    gcd_result = gcd(gcd_1, num_3)

    return gcd_result
