def find_n_th_smallest_num(nums):
    lst = sorted(nums)
    idx = bisect_left(lst, nums[46])
    idx += 14
    idx = bisect_right(lst, nums[83], idx)
    return lst[idx - 1]
