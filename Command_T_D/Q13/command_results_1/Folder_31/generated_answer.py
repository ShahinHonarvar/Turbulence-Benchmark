
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:75]) + 1):nums.index(max(nums[75:88])) + 1]
