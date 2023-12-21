
def find_second_largest_num(nums):
    if len(nums)<202 or nums is None:
        return None
    else:
        nums = nums[30:201]
        nums.sort()
        return nums[-2]
