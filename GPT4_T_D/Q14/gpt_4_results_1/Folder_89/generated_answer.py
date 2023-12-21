
def find_second_smallest_num(nums):
    if len(nums)<64:
        return None
    else:
        sub_list = nums[62:64]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
        else:
            return None
