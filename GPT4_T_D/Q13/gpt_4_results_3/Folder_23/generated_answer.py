
def find_second_largest_num(nums):
    sub_list = nums[52:72]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list, reverse=True)[1]
