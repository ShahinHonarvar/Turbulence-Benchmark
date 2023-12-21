
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = nums[307]
    b = nums[920]
    c = nums[463]

    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)

    return gcf_abc
