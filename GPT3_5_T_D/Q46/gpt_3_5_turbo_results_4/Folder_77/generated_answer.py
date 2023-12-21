
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    x = nums[693]
    y = nums[331]
    z = nums[668]

    gcd_xy = gcd(x, y)
    gcd_xyz = gcd(gcd_xy, z)

    return gcd_xyz
