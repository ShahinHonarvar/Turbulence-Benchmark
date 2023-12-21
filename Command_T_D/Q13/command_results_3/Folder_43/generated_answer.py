
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:68]))+68:nums.index(max(nums[:86]))+86]
