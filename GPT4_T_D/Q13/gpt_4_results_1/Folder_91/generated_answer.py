
def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    else:
        sorted_lst = sorted(lst[:6], reverse=True)
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]
