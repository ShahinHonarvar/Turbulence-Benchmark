
def find_second_largest_num(nums):
    if len(nums) < 81:
        return None
    else:
        partial_list = nums[40:81]
        partial_list.sort()
        return partial_list[-2] if len(partial_list) >= 2 else None
