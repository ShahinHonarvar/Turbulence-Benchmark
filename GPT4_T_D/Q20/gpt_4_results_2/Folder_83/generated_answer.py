
def find_n_th_smallest_num(nums):
    if 30 <= len(nums) <= 300:
        sorted_nums = sorted(nums[30:301])
        return sorted_nums[14]
    else:
        return "The list should have between 30 and 300 elements"
