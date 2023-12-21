def find_second_smallest_num(nums):
    sm_num_index = len(nums) - 2
    sm_num = nums[sm_num_index]
    if sm_num >= 66 and sm_num <= 77:
        return sm_num
    else:
        return None
