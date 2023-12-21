
def find_second_largest_num(lst):
    if len(lst) >= 37:
        target_lst = lst[33:37]
        target_lst.sort()
        return target_lst[-2]
    else:
        return None
