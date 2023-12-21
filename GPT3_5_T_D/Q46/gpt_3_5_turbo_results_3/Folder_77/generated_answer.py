
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x = nums[693]
    y = nums[331]
    z = nums[668]
    
    gcf_xy = gcd(x, y)
    gcf_xyz = gcd(gcf_xy, z)
    
    return gcf_xyz
