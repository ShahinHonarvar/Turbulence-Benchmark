
def gcf_two_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return find_gcd(nums[18], nums[37])
