
def find_second_smallest_num(nums):
    sub_list = nums[43:52]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
