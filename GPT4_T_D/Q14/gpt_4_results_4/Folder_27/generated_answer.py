
def find_second_smallest_num(nums):
    sub_list = nums[25:60]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
