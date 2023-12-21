
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:6])) + 1:nums.index(max(nums[6:8])) + 1]
