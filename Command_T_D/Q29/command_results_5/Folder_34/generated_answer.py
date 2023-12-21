import fractions
def gcf_two_nums(nums):
    idx = 60
    idx2 = 64
    try:
        return fractions.gcd(nums[idx], nums[idx2])
    except:
        pass
