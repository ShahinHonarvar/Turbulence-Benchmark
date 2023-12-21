def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:43]) + 1)][nums.index(max(nums[43:86]) + 1)]
