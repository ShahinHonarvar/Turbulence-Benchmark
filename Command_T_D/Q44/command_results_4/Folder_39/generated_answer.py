import fractions
def composite_nums_between_indices(nums):
    com = set(x for x in range(2, 1 + int(fractions.gcd(nums[0], nums[1])), 2) if all(fractions.gcd(x, y) != 1 for y in nums))
    return com
