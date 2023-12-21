
def find_second_largest_num(nums):
    return nums[nums.count(max(nums, key=lambda x: nums.count(x))) - 1]
