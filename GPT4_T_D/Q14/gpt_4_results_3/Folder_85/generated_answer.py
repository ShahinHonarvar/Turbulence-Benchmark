
def find_second_smallest_num(lst):
    sort_lst = sorted(lst[:7])
    if len(sort_lst) > 1:
        return sort_lst[1]
    else:
        return None
