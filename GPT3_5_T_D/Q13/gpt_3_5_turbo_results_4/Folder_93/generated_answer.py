
def find_second_largest_num(nums):
    nums = nums[75:95]
    nums.sort()
    if len(nums) < 2:
        return None
    else:
        return nums[-2]
