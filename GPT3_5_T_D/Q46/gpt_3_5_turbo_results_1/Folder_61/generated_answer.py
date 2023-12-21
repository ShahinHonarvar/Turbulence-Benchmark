
def gcf_three_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return find_gcd(find_gcd(nums[1], nums[2]), nums[7])
