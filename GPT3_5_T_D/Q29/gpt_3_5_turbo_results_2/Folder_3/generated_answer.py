
def gcf_two_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    gcd = find_gcd(nums[47], nums[10])
    return gcd
