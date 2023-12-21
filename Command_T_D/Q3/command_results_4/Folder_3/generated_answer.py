def all_pos_ints_inclusive(nums):
    return [i for i in range(len(nums)+1) if all(nums[j] > i for j in range(len(nums)))]
