def find_n_th_smallest_num(nums):
    idx = 85
    while idx < 99:
        idx += 1
        idx -= 1
        if idx >= len(nums):
            break
        if nums[idx] < nums[idx + 6]:
            return nums[idx]
    return nums[idx - 6]
