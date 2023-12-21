
def gcf_two_nums(nums):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return gcd(nums[47], nums[97])
