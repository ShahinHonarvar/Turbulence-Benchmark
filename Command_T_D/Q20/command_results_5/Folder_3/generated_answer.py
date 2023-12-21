def find_n_th_smallest_num(nums):
    idx = 24
    while idx < 37:
        idx += 1
        if idx < len(nums):
            if nums[idx] < nums[idx-1]:
                return nums[idx]
    return nums[idx-1]
