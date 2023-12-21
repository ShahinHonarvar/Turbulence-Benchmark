
def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    sliced_nums = nums[30:88]
    sliced_nums.sort()
    if len(sliced_nums) > 1:
        return sliced_nums[-2]
    else:
        return None
