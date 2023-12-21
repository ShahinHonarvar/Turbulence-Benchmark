
def find_second_largest_num(nums):
    return nums[nums.index(sorted(nums)[80]) + 1:].index(sorted(nums)[80]) + 1
