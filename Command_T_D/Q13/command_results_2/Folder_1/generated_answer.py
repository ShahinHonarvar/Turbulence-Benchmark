
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:31])) + 1:nums.index(max(nums[31:72])) + 2]
