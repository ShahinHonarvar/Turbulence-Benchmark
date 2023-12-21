
def find_second_largest_num(nums):
    sub_list = nums[34:56]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
