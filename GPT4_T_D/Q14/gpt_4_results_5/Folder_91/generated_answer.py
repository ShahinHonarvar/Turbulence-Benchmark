
def find_second_smallest_num(lst):
    if len(lst) < 6:
        return None
    else:
        lst_to_index_5 = lst[0:6]
        lst_to_index_5.sort()
        return lst_to_index_5[1]
