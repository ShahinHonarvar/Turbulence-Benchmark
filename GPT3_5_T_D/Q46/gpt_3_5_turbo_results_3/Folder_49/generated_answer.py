
def gcf_three_nums(nums):
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return compute_gcd(compute_gcd(nums[34], nums[38]), nums[77])
