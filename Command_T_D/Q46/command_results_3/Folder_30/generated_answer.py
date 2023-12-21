
def gcf_three_nums(nums):
    return max(x for x in range(min(nums),1, -1) if all(x == gcd(x, y) for y in nums[76:]))
