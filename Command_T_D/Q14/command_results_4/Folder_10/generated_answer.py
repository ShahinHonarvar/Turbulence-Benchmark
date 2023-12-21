def find_second_smallest_num(nums):
    return nums[nums.count(min(nums)) + 62:nums.count(min(nums)) + 92]
