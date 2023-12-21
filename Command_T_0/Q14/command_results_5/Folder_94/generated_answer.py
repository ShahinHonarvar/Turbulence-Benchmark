def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[52]) + 1:nums.index(sorted(nums)[71]) + 1]
