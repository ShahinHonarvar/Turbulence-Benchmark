
def gcf_three_nums(nums):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    return gcd(gcd(nums[76], nums[64]), nums[28])
