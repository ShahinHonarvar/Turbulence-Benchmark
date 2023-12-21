
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:37] + nums[37:76] + nums[76:])) - 1]
