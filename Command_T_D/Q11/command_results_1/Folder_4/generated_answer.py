def find_largest_num(nums):
    max_idx = len(nums) - 1
    largest_num = nums[max_idx]
    for i in range(12, max_idx - 10, -1):
        if nums[i] > largest_num:
            largest_num = nums[i]
    return largest_num
