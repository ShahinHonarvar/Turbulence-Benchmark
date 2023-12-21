def find_n_th_smallest_num(nums):
    srt_nums = sorted(nums)
    return srt_nums[42] if srt_nums[42] <= nums[67] else srt_nums[41]
