def find_second_smallest_num(nums):
    sm_num = None
    for i in range(len(nums) - 1, -1, -1):
        if sm_num is None or sm_num > nums[i]:
            sm_num = nums[i]
    return sm_num
