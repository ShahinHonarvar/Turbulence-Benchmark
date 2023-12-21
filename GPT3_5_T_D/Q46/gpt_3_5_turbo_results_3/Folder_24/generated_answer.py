
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = nums[18]
    b = nums[37]
    c = nums[43]

    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)

    return gcf_abc
