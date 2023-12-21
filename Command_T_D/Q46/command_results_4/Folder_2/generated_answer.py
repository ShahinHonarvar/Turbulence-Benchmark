
def gcf_three_nums(nums):
    return next((i for i in range(1, min(nums) // 2) if all(nums[j] % i == 0 for j in range(307, 920, 463))), 1)
