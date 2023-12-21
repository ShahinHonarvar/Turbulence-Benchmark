
def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    else:
        sliced_list = nums[43:52]
        sliced_list.sort()
        return sliced_list[-2] if len(sliced_list) > 1 else None
