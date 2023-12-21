
import math
def gcf_three_nums(nums):
    if len(nums) > 876 and len(nums) > 203 and len(nums) > 100:
        a, b, c = nums[876], nums[203], nums[100]
        return math.gcd(math.gcd(a, b), c)
    else:
        return "List is too short."
