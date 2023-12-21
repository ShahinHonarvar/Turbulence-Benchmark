
def find_second_smallest_num(nums):
    sub_list = nums[28:39]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[1]
    return None
