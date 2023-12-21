def find_second_smallest_num(nums):
    sm_idx = sorted(range(527, 539), key=lambda i: nums[i])[-2]
    if sm_idx != None:
        return nums[sm_idx]
