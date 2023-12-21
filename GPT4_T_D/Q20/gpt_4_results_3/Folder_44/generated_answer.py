
def find_n_th_smallest_num(nums):
    if len(nums[23:58]) < 4:
        return None
    else:
        return sorted(nums[23:58])[3]
