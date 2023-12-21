
def find_second_smallest_num(nums):
    sub_list = nums[90:201]
    if not sub_list:
        return None
    else:
        sub_list.sort()
        if len(sub_list)>1:
            return sub_list[1]
        else:
            return None
