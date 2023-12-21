
def find_second_largest_num(lst):
    if len(lst) >= 40:
        short_lst = lst[40:201]
        if len(short_lst) < 2:
            return None
        else:
            short_lst.sort()
            return short_lst[-2]
    else:
        return None
