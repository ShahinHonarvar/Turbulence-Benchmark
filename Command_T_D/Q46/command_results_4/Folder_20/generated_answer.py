
def gcf_three_nums(nums):
    return max(x for x in range(1, nums[29] // 2) if all(x == y or x % y == 0) for y in (nums[29], nums[53], nums[42]))
