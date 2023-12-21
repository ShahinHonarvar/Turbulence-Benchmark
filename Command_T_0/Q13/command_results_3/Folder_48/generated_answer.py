def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:533]) + 1):nums.index(max(nums[533:605])) + 1]
