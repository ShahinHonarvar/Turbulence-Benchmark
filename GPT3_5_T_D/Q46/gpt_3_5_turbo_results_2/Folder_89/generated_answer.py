
def gcf_three_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    a = nums[63]
    b = nums[73]
    c = nums[11]
    
    gcd1 = find_gcd(a, b)
    gcd2 = find_gcd(gcd1, c)
    
    return gcd2
