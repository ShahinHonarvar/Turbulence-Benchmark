import set as s
import operator as o
def composite_nums_between_indices(nums):
    return s.set(nums[60:200]) & s.set(o.gcd(nums[60:200], 2))
