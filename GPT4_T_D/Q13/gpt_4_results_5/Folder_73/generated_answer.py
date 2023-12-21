
def find_second_largest_num(lst):
    if not lst or len(lst) < 92:
        return None
    sliced_list = lst[19:93]
    sliced_list.sort()
    return None if len(sliced_list) < 2 else sliced_list[-2]
