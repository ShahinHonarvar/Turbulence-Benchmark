def find_n_th_smallest_num(nums):
    if len(nums) < 40 or len(nums) < 75:
        return None
    end_idx = nums.index(max(nums)) + 1
    return nums[end_idx - 40]
