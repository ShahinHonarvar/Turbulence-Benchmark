
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:62]) + 1):nums.index(max(nums[62:78])) + 1]
