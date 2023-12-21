def find_second_smallest_num(nums):
    sm_nums = sorted(nums)
    sm_nums = sm_nums[1:100] + [sm_nums[0]]
    if len(sm_nums) == 0:
        return None
    return sm_nums[1]
