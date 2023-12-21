
import fractions as cf

def gcf_three_nums(nums):
    g = 1
    for i in range(3):
        g = cf.gcd(g, nums[i])
    return g
