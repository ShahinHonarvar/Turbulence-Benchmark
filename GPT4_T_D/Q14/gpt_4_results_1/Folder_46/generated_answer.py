
def find_second_smallest_num(lst):
    sliced_lst = lst[13:69]
    sliced_lst.sort()

    if len(sliced_lst) < 2:
        return None
    else:
        return sliced_lst[1]
