
def find_second_largest_num(nums):
    if len(nums)<10:
        return None
    else:
        sub_list = nums[8:10]
        sub_list.sort(reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
