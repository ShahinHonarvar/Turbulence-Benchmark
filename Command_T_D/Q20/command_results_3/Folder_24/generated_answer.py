def find_n_th_smallest_num(nums):
    idx = 43
    while idx < len(nums):
        if idx < n: break
        idx += 1
    idx = 80
    while idx >= n:
        if idx >= len(nums): break
        idx -= 1
    return nums[idx]
