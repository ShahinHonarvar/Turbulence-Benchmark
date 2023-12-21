
def find_second_smallest_num(nums):
    try:
        sub_list = nums[533:606]
        sub_list.sort()
        return sub_list[1]
    except IndexError:
        return None
