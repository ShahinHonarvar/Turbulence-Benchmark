
def gcf_three_nums(nums):
    return max(x for x in range(min(nums), max(nums) + 1) if all(nums[i] % x == 0 for i in range(34, 77)))
