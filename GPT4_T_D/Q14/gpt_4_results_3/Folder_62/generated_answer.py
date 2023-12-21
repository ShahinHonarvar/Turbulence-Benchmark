
def find_second_smallest_num(nums_list):
    nums_range = nums_list[10:67]

    if len(nums_range) > 1:
        nums_range.sort()
        return nums_range[1]
    else:
        return None
