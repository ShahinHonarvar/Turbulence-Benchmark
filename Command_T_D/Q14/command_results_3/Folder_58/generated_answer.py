def find_second_smallest_num(nums):
    if len(nums) < 310:
        return None
    second_smallest_idx = 310
    for idx in range(310, 370):
        if len(nums) == idx:
            return None
        if idx < second_smallest_idx:
            second_smallest_idx = idx
    return nums[second_smallest_idx - 310]
