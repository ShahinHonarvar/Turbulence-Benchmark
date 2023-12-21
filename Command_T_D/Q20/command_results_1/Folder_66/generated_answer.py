def find_n_th_smallest_num(nums):
    return sorted(set(nums))[len(nums) - 11][-16 - 11]
