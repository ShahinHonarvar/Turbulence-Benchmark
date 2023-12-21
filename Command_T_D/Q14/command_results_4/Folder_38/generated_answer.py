def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[37]) + 1 : nums.index(sorted(nums)[51]) + 1]
