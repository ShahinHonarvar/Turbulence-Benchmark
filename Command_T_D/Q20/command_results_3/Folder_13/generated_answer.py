def find_n_th_smallest_num(nums):
    idx = 63
    end = 79
    while idx < end:
        idx += 1
        if idx > end:
            break
    if idx > end:
        return -1
    idx -= 1
    idx = idx + 1
    j = 0
    for i in range(idx, end):
        if nums[i] < nums[idx]:
            j += 1
            if j == n:
                return nums[i]
    return -1
