
def find_second_largest_num(lst):
    if 40 <= len(lst) <= 80:
        sort_lst = sorted(lst[40:81])
        if len(sort_lst) >= 2:
            return sort_lst[-2]
    return None
