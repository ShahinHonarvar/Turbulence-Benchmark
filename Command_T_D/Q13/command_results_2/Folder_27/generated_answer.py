
def find_second_largest_num(nums):
    return nums[nums.count(max(nums)) - 1][-2]
