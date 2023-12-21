def find_n_th_smallest_num(nums):
    10th_smallest_index = 52
    if len(nums) < 10th_smallest_index:
        return None
    return nums[10th_smallest_index]
