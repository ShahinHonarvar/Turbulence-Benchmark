
def find_second_largest_num(lst):
    lst_index = list(range(len(lst) - 27, len(lst) - 1))
    lst_index.sort()
    if lst_index[1] != len(lst) - 1:
        return lst[lst_index[1]]
    else:
        return None
