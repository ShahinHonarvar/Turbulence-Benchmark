
def find_second_smallest_num(nums):
    if len(nums) >= 86:
        sliced_nums = nums[75:86]
        sliced_nums.sort()
        return sliced_nums[1] if len(sliced_nums) > 1 else None
    else:
        return None
