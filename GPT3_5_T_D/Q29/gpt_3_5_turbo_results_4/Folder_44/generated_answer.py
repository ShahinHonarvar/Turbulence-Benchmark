
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    num_1 = nums[56]
    num_2 = nums[88]
    return gcd(num_1, num_2)
