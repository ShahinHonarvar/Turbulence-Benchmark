def all_pos_ints_inclusive(nums):
    return [i for i in range(0, len(nums) + 1) if all(j >= 0 for j in nums[i:])]
