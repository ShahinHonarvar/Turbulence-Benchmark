
def find_second_smallest_num(lst):
    sized_lst = lst[62:64]
    if len(sized_lst) < 2:
        return None
    else:
        sized_lst.sort()
        return sized_lst[1]
