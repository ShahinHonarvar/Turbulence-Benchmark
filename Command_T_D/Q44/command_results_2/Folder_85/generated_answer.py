def composite_nums_between_indices(nums):
    if 3 <= len(nums) <= 5:
        if nums[2] == 2:
            return set(nums[3:])
        else:
            return set(nums[3:-1])
    else:
        return set()
