
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num_a = nums[91]
    num_b = nums[45]

    return gcd(num_a, num_b)
