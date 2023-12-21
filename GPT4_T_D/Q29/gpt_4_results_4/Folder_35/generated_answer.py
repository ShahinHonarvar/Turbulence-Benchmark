
def gcf_two_nums(nums):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    return gcd(nums[380], nums[327])
