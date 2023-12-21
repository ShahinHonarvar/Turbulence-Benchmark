def find_n_th_smallest_num(nums):
    srt = sorted(set(nums))
    return srt[nums.index(srt[11]) + 12]
