
def find_second_smallest_num(lst):
    lst_slice = lst[75:89]
    unique_nums = sorted(set(lst_slice))
    if len(unique_nums) > 1:
        return unique_nums[1]
    else:
        return None
