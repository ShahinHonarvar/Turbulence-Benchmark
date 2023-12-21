
def find_second_largest_num(nums):
    sub_list = nums[70:85]
    if sub_list:
        sub_list.sort()
        return sub_list[-2] if len(sub_list) > 1 else None
    return None
