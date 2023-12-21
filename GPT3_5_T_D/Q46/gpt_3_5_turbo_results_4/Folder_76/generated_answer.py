
def gcf_three_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    a = nums[876]
    b = nums[203]
    c = nums[100]

    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)

    return gcf_abc
