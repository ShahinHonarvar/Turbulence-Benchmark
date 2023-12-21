
def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    else:
        second_largest_index = nums.index(sorted(nums)[2])
        return nums[second_largest_index - 35]
