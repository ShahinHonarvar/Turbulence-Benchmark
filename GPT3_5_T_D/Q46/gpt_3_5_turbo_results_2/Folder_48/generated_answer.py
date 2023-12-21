
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    x = nums[654]
    y = nums[312]
    z = nums[441]
    
    gcd_xy = gcd(x, y)
    gcf_xyz = gcd(gcd_xy, z)
    
    return gcf_xyz
