
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:30], key=lambda x: x)) + 1:nums.index(max(nums[30:48], key=lambda x: x)) + 1]
