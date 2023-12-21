
def gcf_three_nums(nums):
    gcf = 1
    for n in nums:
        gcf = gcf * n // gcd(gcf, n)
    return gcf
