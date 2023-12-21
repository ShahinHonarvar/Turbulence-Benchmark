
def find_second_largest_num(nums):
    sub_list = nums[82:87]
    if len(sub_list) == 0:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
