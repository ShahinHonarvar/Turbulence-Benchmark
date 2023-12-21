
def gcf_three_nums(nums):
    return max(x for x in range(1, min(nums) + 1) if all(y % x == 0 for y in nums))
