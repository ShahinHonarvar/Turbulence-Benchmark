def find_n_th_smallest_num(nums):
    idx = 82
    while idx < 93:
        if nums[idx] < nums[idx - 1]:
            idx += 1
        else:
            break
    return nums[idx - 1]
