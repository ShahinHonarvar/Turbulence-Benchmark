def find_second_smallest_num(nums):
    if len(nums) < 24:
        return
    elif len(nums) == 24:
        return nums[22]
    else:
        return nums[23]
