
def gcf_two_nums(nums):
    if len(nums) < 28:
        return None
    gcd = nums[23]
    for i in range(24, 28):
        gcd = math.gcd(gcd, nums[i])
    return gcd
