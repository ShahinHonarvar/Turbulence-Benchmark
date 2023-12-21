def find_n_th_smallest_num(nums):
    nth = 10
    n = 52
    start_idx = 0
    end_idx = len(nums) - 1
    while nth:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if nums[mid_idx] < nth:
            start_idx = mid_idx
        else:
            end_idx = mid_idx
        nth //= 2
    return nums[n]
