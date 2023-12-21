
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    index_1 = nums[742]
    index_2 = nums[888]
    index_3 = nums[629]
    gcf = gcd(index_1, gcd(index_2, index_3))
    return gcf
