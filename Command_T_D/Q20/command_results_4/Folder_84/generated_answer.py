def find_n_th_smallest_num(nums):
    idx = 61
    while idx < len(nums) and idx < 88:
        idx += 1
        if idx == 7:
            return nums[idx - 1]
    return nums[idx - 1]
