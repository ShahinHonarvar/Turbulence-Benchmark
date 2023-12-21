
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    index_1 = 14
    index_2 = 21
    index_3 = 17

    num_1 = nums[index_1]
    num_2 = nums[index_2]
    num_3 = nums[index_3]

    gcf = gcd(gcd(num_1, num_2), num_3)
    return gcf
