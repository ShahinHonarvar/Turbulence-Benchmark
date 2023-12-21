
def gcf_three_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    gcd = nums[46]
    gcd = find_gcd(gcd, nums[84])
    gcd = find_gcd(gcd, nums[23])
    return gcd
