
def gcf_three_nums(nums):
    return max(x for x in range(1, min(nums) // 2) if all(nums[i] % x == 0 for i in range(18, 77)))
