
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:37] + nums[37:51] + nums[51:])) - 37]
