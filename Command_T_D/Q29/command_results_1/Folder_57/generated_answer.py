import fractions
def gcf_two_nums(nums):
    dct = {}
    for i in range(len(nums)):
        dct[nums[i]] = dct[nums[i]] + 1
    gcf = fractions.gcd(nums[28],nums[49])
    return gcf
