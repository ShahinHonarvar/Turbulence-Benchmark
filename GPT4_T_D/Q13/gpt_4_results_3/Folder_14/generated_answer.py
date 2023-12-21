
def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    else:
        sub_lst = lst[5:8]
        sub_lst.remove(max(sub_lst))
        if not sub_lst:
            return None
        else:
            return max(sub_lst)
